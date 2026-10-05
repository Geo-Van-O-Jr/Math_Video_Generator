"""Render independent Manim modules, cache them, and concatenate a silent MP4."""
import argparse
import importlib.metadata
import json
import os
from pathlib import Path
import subprocess
import sys
import yaml
from config import ROOT, PROFILES
from engine.utils.render_utils import executable, fingerprint, concatenate


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("episode")
    quality = parser.add_mutually_exclusive_group()
    quality.add_argument("--preview", action="store_true")
    quality.add_argument("--final", action="store_true")
    parser.add_argument("--scene", type=int, help="One-based scene number")
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()
    episode = ROOT / "episodes" / args.episode
    if episode.parent != ROOT / "episodes" or not episode.is_dir():
        parser.error("Unknown episode")
    metadata = yaml.safe_load((episode / "episode.yaml").read_text(encoding="utf-8"))
    order = metadata["scene_order"]
    if args.scene is not None and not 1 <= args.scene <= len(order):
        parser.error(f"--scene must be between 1 and {len(order)}")
    executable("latex")
    executable("dvisvgm")
    ffmpeg = executable("ffmpeg")
    profile = "final" if args.final else "preview"
    settings = PROFILES[profile]
    shared = list((ROOT / "engine").rglob("*.py")) + [ROOT / "config.py", ROOT / "build.py",
                                                        episode / "episode.yaml"]
    out = episode / "output"
    cache_path = out / f"cache_{profile}.json"
    out.mkdir(parents=True, exist_ok=True)
    cache = json.loads(cache_path.read_text()) if cache_path.exists() else {}
    env = os.environ.copy()
    env["PYTHONPATH"] = str(ROOT) + os.pathsep + env.get("PYTHONPATH", "")
    env["PYTHONIOENCODING"] = "utf-8"
    env["MATH_VIDEO_SCENE_COUNT"] = str(len(order))
    clips = []
    for index, module in enumerate(order, 1):
        if args.scene is not None and index != args.scene:
            continue
        source = episode / "scenes" / f"{module}.py"
        media = episode / "media" / profile / module
        clip_dir = out / "clips" / profile
        clip_dir.mkdir(parents=True, exist_ok=True)
        target = clip_dir / f"{module}.mp4"
        signature = fingerprint(shared + [source], (settings, importlib.metadata.version("manim"),
                                                    sys.version, "cairo"))
        if args.force or cache.get(module) != signature or not target.exists():
            print(f"Rendering {index}/{len(order)}: {module}", flush=True)
            command = [sys.executable, "-m", "manim", "--renderer", "cairo",
                       "--disable_caching", "--media_dir", str(media),
                       "-r", settings["resolution"], "--fps", str(settings["fps"]),
                       "--format", "mp4", "-o", module, str(source), "EpisodeScene"]
            log = out / f"{module}_{profile}.log"
            with log.open("w", encoding="utf-8") as handle:
                result = subprocess.run(command, cwd=ROOT, env=env, stdout=handle,
                                        stderr=subprocess.STDOUT)
            if result.returncode:
                raise RuntimeError(f"Scene {index} failed. Read {log}\n" +
                                   log.read_text(encoding="utf-8")[-5000:])
            candidates = [p for p in media.rglob(f"{module}.mp4")
                          if "partial_movie_files" not in p.parts]
            if len(candidates) != 1:
                raise RuntimeError(f"Expected exactly one rendered clip: {candidates}")
            import shutil
            shutil.copy2(candidates[0], target)
            cache[module] = signature
            cache_path.write_text(json.dumps(cache, indent=2), encoding="utf-8")
        else:
            print(f"Cached: {module}", flush=True)
        clips.append(target)
    if args.scene is not None:
        print(f"Scene ready: {clips[0]}")
        return
    final = out / f"{args.episode}_{profile}.mp4"
    concatenate(clips, final, ffmpeg)
    print(f"Video ready: {final}")


if __name__ == "__main__":
    try:
        main()
    except (RuntimeError, subprocess.CalledProcessError) as exc:
        print(f"BUILD FAILED: {exc}", file=sys.stderr)
        sys.exit(1)
