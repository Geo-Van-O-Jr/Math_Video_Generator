"""Decode the video and create contact sheets for every stable reading cue."""
import argparse
import json
import subprocess
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import yaml
from PIL import Image, ImageDraw
from config import ROOT, PROFILES
from engine.utils.render_utils import executable


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
    durations = []
    summary = []
    expected_width, expected_height = map(int, PROFILES[profile]["resolution"].split(","))
    for i, module in enumerate(order, 1):
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
    (audit / "report.json").write_text(json.dumps(report, indent=2))
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
