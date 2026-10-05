"""Decode the video and create contact sheets for every stable reading cue."""
import argparse
import hashlib
import importlib.metadata
import html
import json
import subprocess
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import yaml
from PIL import Image, ImageDraw, ImageChops, ImageStat
from config import ROOT, PROFILES
from engine.utils.render_utils import executable, fingerprint


def probe(path):
    return json.loads(subprocess.check_output([executable("ffprobe"), "-v", "error",
        "-show_streams", "-show_format", "-of", "json", str(path)], text=True))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("episode")
    parser.add_argument("--preview", action="store_true")
    parser.add_argument("--final", action="store_true")
    args = parser.parse_args()
    profile = "final" if args.final else "preview"
    ep = ROOT / "episodes" / args.episode
    order = yaml.safe_load((ep / "episode.yaml").read_text())["scene_order"]
    out = ep / "output"
    audit = out / f"inspection_{profile}"
    audit.mkdir(exist_ok=True)
    ffmpeg = executable("ffmpeg")
    frames = []
    reference_frames = {}
    boundaries = []
    durations = []
    summary = []
    expected_width, expected_height = map(int, PROFILES[profile]["resolution"].split(","))
    shared=(list((ROOT/'engine').rglob('*.py'))+
            list((ROOT/'engine'/'assets').glob('*.svg'))+list(ep.glob('*.py'))+
            [ROOT/'config.py',ROOT/'build.py',ep/'episode.yaml'])
    source_signature=fingerprint(shared+list((ep/'scenes').glob('*.py')),PROFILES[profile])
    cache=json.loads((out/f'cache_{profile}.json').read_text())
    if yaml.safe_load((ep/'episode.yaml').read_text()).get('requires_preview_approval'):
        final=out/f'{args.episode}_{profile}.mp4'
        manifest=json.loads(final.with_suffix('.build.json').read_text())
        assert manifest['source_fingerprint']==source_signature, 'Full build is stale; rebuild first'
        with final.open('rb') as handle:
            assert manifest['video_sha256']==hashlib.file_digest(handle,'sha256').hexdigest(), 'Video changed since full build'
    for i, module in enumerate(order, 1):
        expected_signature=fingerprint(shared+[ep/'scenes'/f'{module}.py'],
            (PROFILES[profile],importlib.metadata.version('manim'),sys.version,'cairo'))
        assert cache.get(module)==expected_signature, f'{module} preview is stale; rebuild first'
        clip = out / "clips" / profile / f"{module}.mp4"
        info = probe(clip)
        assert len(info["streams"]) == 1 and info["streams"][0]["codec_type"] == "video"
        video = info["streams"][0]
        assert (video["width"], video["height"]) == (expected_width, expected_height)
        num, den = map(int, video["avg_frame_rate"].split("/"))
        assert num / den == PROFILES[profile]["fps"]
        duration = float(info["format"]["duration"])
        durations.append(duration)
        # Decode the entire clip: checks every frame, not merely the container.
        subprocess.run([ffmpeg, "-v", "error", "-xerror", "-i", str(clip),
                        "-f", "null", "-"], check=True, capture_output=True)
        cues = json.loads((ep / "media" / profile / module / "cues" / "EpisodeScene.json").read_text())
        for j, cue in enumerate(cues, 1):
            frame = audit / f"{i:02d}_{j:02d}.png"
            subprocess.run([ffmpeg, "-v", "error", "-y", "-ss", str(cue["time"]),
                            "-i", str(clip), "-frames:v", "1", "-vf", "scale=640:360",
                            str(frame)], check=True, capture_output=True)
            frames.append((frame, f"Scene {i:02d} / beat {j:02d} / {cue['time']:.1f}s"))
            if (ep / "references" / f"{cue['caption']}.png").exists():
                keyframe = audit / f"keyframe_{cue['caption']}.png"
                subprocess.run([ffmpeg, "-v", "error", "-y", "-ss", str(cue["time"]),
                                "-i", str(clip), "-frames:v", "1", str(keyframe)],
                               check=True, capture_output=True)
                reference_frames[cue['caption']] = {"scene": module,
                    "local_seconds": cue['time'],
                    "video_seconds": sum(durations[:-1])+cue['time']}
                sheet = Image.new("RGB", (expected_width*2,expected_height+32), "#10151E")
                with Image.open(ep / "references" / f"{cue['caption']}.png") as ref:
                    sheet.paste(ref.convert("RGB").resize((expected_width,expected_height)),(0,32))
                with Image.open(keyframe) as rendered:
                    sheet.paste(rendered.convert("RGB"),(expected_width,32))
                draw=ImageDraw.Draw(sheet)
                draw.text((10,8),"Provided visual reference (mathematical errors corrected in film)",fill="white")
                draw.text((expected_width+10,8),"Reconstructed Manim composition",fill="white")
                sheet.save(audit / f"comparison_{cue['caption']}.png")
        ends=[]
        for suffix,when in (("first",0),("last",max(0,duration-1/PROFILES[profile]['fps']))):
            endpoint=audit / f"{i:02d}_{suffix}.png"
            subprocess.run([ffmpeg,"-v","error","-y","-ss",str(when),"-i",str(clip),
                            "-frames:v","1",str(endpoint)],check=True,capture_output=True)
            ends.append(endpoint)
        boundaries.append(ends)
        summary.append({"scene": module, "duration": duration, "reading_cues": len(cues)})
    final = out / f"{args.episode}_{profile}.mp4"
    info = probe(final)
    assert len(info["streams"]) == 1 and info["streams"][0]["codec_type"] == "video"
    assert abs(float(info["format"]["duration"]) - sum(durations)) < 0.5
    subprocess.run([ffmpeg, "-v", "error", "-xerror", "-i", str(final), "-f", "null", "-"],
                   check=True, capture_output=True)
    for start in range(0, len(frames), 12):
        sheet = Image.new("RGB", (1280, 6 * 388), "#10151F")
        draw = ImageDraw.Draw(sheet)
        for index, (frame, label) in enumerate(frames[start:start+12]):
            x, y = (index % 2) * 640, (index // 2) * 388
            with Image.open(frame) as im:
                sheet.paste(im, (x, y))
            draw.text((x + 10, y + 364), label, fill="white")
        sheet.save(audit / f"contact_{start // 12 + 1:02d}.jpg")
    report = {"profile": profile, "duration_seconds": sum(durations),
              "audio_streams": 0, "all_frames_decoded": True, "scenes": summary}
    joins=[]
    for index in range(len(boundaries)-1):
        with Image.open(boundaries[index][1]) as before, Image.open(boundaries[index+1][0]) as after:
            difference=ImageChops.difference(before.convert('RGB'),after.convert('RGB'))
            mae=sum(ImageStat.Stat(difference).mean)/3
            joins.append({"after_scene":index+1,"mean_absolute_rgb_error":mae})
    report["boundary_comparisons"]=joins
    report["keyframes"]=reference_frames
    # A separate uniform-time audit exposes slideshow-like resets and unearned frames.
    for page,start in enumerate(range(0,int(sum(durations)),8*12),1):
        subprocess.run([ffmpeg,"-v","error","-y","-ss",str(start),"-i",str(final),
                        "-vf","fps=1/8,scale=427:240,tile=3x4","-frames:v","1",
                        str(audit/f"eight_seconds_{page:02d}.jpg")],check=True,capture_output=True)
    report['source_fingerprint']=source_signature
    with final.open('rb') as handle:
        report['video_sha256']=hashlib.file_digest(handle,'sha256').hexdigest()
    (audit / "report.json").write_text(json.dumps(report, indent=2))
    if reference_frames:
        labels={'problem_statement':'Enunciado', 'game_geometry':'Geometria do jogo',
                'two_worlds':'Duas rotas indistinguíveis',
                'quantitative_conclusion':'Conclusão quantitativa'}
        buttons=''.join(f'<button onclick="seek({cue["video_seconds"]:.3f})">{html.escape(labels.get(name,name))}</button>'
                        for name,cue in reference_frames.items())
        comparisons=''.join(f'<section><h2>{html.escape(labels.get(name,name))}</h2>'
            f'<p>Referência à esquerda; reconstrução em Manim à direita. '
            f'Instante {cue["video_seconds"]:.1f}s.</p>'
            f'<a href="inspection_{profile}/comparison_{name}.png"><img '
            f'src="inspection_{profile}/comparison_{name}.png" alt="Comparação visual"></a></section>'
            for name,cue in reference_frames.items())
        clips=''.join(f'<li><a href="clips/{profile}/{module}.mp4">{html.escape(module)}</a></li>' for module in order)
        document=f'''<!doctype html><html lang="pt-BR"><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>IMO 2017 P3 · Revisão da prévia</title><style>
body{{margin:0;background:#10151e;color:#e9ecf5;font:17px/1.6 Georgia,serif}}
main{{max-width:1100px;margin:auto;padding:32px 24px}}h1{{font-weight:400}}
video,img{{width:100%;border-radius:8px}}video{{background:#10151e}}
nav{{display:flex;gap:10px;flex-wrap:wrap;margin:20px 0}}
button{{background:#1c2838;color:#c8e4ff;border:1px solid #53799f;border-radius:6px;padding:10px 16px;cursor:pointer}}
a{{color:#8fcaff}}section{{margin:54px 0}}p,li{{color:#afbdd1}}h2{{font-weight:400}}
.facts{{padding:16px 22px;border-left:2px solid #65debb;background:#142125}}
</style><main><h1>IMO 2017 · Problem 3</h1>
<p>Prévia completa · {sum(durations)/60:.2f} minutos · {expected_width} × {expected_height} · {PROFILES[profile]['fps']} fps · sem áudio</p>
<video id="film" controls preload="metadata" poster="inspection_{profile}/keyframe_two_worlds.png" src="{args.episode}_{profile}.mp4"></video>
<nav>{buttons}</nav>
<div class="facts">O vídeo final em 1080p / 60 fps aguarda sua aprovação desta prévia.
A matemática foi conferida com o enunciado e a solução oficiais. As imagens de referência orientam o estilo; seus erros matemáticos foram corrigidos.</div>
<p><a href="../screenplay.md">Roteiro</a> · <a href="../sources/README.md">Fontes e verificação matemática</a> ·
<a href="inspection_{profile}/report.json">Relatório técnico</a></p>
{comparisons}<section><h2>Segmentos de produção</h2><p>Arquivos independentes para revisão. A numeração não aparece no filme.</p><ul>{clips}</ul></section>
<script>function seek(t){{const v=document.getElementById('film');v.currentTime=t;v.scrollIntoView({{behavior:'smooth',block:'center'}});}}</script></main></html>'''
        (out/'review.html').write_text(document,encoding='utf-8')
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
