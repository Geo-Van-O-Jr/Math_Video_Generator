import hashlib
import shutil
import subprocess
from pathlib import Path


def executable(name):
    found = shutil.which(name)
    if found:
        return found
    if name == "ffmpeg":
        try:
            import imageio_ffmpeg
            return imageio_ffmpeg.get_ffmpeg_exe()
        except (ImportError, RuntimeError):
            pass
    raise RuntimeError(f"Missing {name}. See README dependency installation.")


def fingerprint(paths, settings):
    digest = hashlib.sha256(repr(settings).encode())
    for path in sorted(paths):
        digest.update(str(path).encode())
        digest.update(path.read_bytes())
    return digest.hexdigest()


def concatenate(clips, output, ffmpeg):
    output.parent.mkdir(parents=True, exist_ok=True)
    manifest = output.with_suffix(".concat.txt")
    # Generated clip names are controlled by build.py; forward slashes work on Windows.
    manifest.write_text("".join(f"file '{p.resolve().as_posix()}'\n" for p in clips),
                        encoding="utf-8")
    temporary = output.with_name(output.stem + ".tmp.mp4")
    subprocess.run([ffmpeg, "-y", "-hide_banner", "-loglevel", "error",
                    "-f", "concat", "-safe", "0", "-i", str(manifest),
                    "-map", "0:v:0", "-c:v", "copy", "-an",
                    "-movflags", "+faststart", str(temporary)], check=True)
    temporary.replace(output)
