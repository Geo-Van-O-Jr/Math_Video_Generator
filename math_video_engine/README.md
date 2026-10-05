# Mathematics Video Engine v0.1

## IMO 2017 Problem 3: persistent proof canvas

The new `imo_2017_p3` episode reconstructs the supplied navy/serif/vector
references as continuous Manim geometry. Its five internal render segments
have no visible chapter system and share exact boundary constructors in
`episodes/imo_2017_p3/visuals.py`. It is silent and uses the official 200-round
argument, with the initial coincident position and the contest's `<=100`
boundary treated explicitly. See its `screenplay.md` and `sources/README.md`.

```powershell
cd math_video_engine
..\.venv\Scripts\python.exe build.py imo_2017_p3 --preview
..\.venv\Scripts\python.exe tools/verify_hunter_rabbit.py
..\.venv\Scripts\python.exe tools/inspect_video.py imo_2017_p3 --preview
# Only after the user approves the reviewed complete preview:
..\.venv\Scripts\python.exe build.py imo_2017_p3 --final --approve-preview
```

The reusable opt-in components live in `engine/components/living_canvas.py`:
`PersistentCanvas`, `ProofWriter` / `EquationDerivation`, `PersistentFact`,
`TrackedPoint` / `MovingPoint`, `UncertaintyDisk`, `DashedTrajectory`,
`DistanceAnnotation`, `SymmetricChoices` and `ResultHighlight`. Canvas cues
are semantic review points, never on-screen slide numbers. Prose is written
line by line; equations transform in place; facts can be pinned and dimmed.
SVG icons live in `engine/assets/`. The original episode's base scene and
theme remain intact.

Build fingerprints now include episode-level Python helpers and SVG assets.
The new episode requires a current inspected preview and explicit approval
before a final render. The approval records a source fingerprint; source
changes invalidate it. Do not pass `--approve-preview` as a substitute for
the user's actual approval.

Inspection decodes all video frames, checks silent profile-conformant clips,
extracts semantic keyframes, creates side-by-side reference comparisons,
exports eight-second contact sheets, and measures pixel differences across
internal boundaries. Outputs are in `output/inspection_preview/`. The
mathematical verifier checks true world coordinates, including common pings,
200 unit-length steps, the minimax endpoint bound and exact round accounting.

---

A local Manim Community project for silent, English mathematics exposition.
The first episode solves IMO Shortlist 2025, Number Theory N3. Its ten
independent scenes follow the supplied proof, with an explicit sufficiency
check added before the conclusion. No audio, services, API keys, or GUI.

The first episode has been rendered and verified in both preview and final
quality. See [VALIDATION.md](VALIDATION.md) for the local results.

## Install (Windows / PowerShell)

Python 3.12, MiKTeX (including `latex` and `dvisvgm`), and FFmpeg are required.
The [official Manim installation guide](https://docs.manim.community/en/stable/installation.html)
describes the underlying dependencies. This project pins Manim CE 0.19.0.

```powershell
winget install -e --id Python.Python.3.12 --scope user
winget install -e --id MiKTeX.MiKTeX --scope user
winget install -e --id Gyan.FFmpeg
# Open a fresh terminal so the updated PATH takes effect.
cd C:\Users\Geovano\Math_Video_Generator
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r math_video_engine\requirements.txt
initexmf --set-config-value '[MPM]AutoInstall=1'
```

MiKTeX must have its package repository initialized. Missing LaTeX packages
can be installed automatically with the above setting; initial compilation
therefore needs internet access. Alternatively, install them explicitly:

```powershell
miktex packages install standalone preview amsmath amsfonts cm-super doublestroke everysel ragged2e relsize fundus-calligra wasysym physics dvisvgm
```

On Linux, install Python/venv, FFmpeg, Cairo/Pango development libraries and
a TeX distribution with `latex`, `dvisvgm`, and the packages in Manim's default
template; create a venv and install `requirements.txt`.

## Render

Run from `math_video_engine` with the virtual environment's interpreter:

```powershell
cd math_video_engine
..\.venv\Scripts\python.exe build.py imo_2025_n3 --preview
..\.venv\Scripts\python.exe build.py imo_2025_n3 --scene 6 --preview
..\.venv\Scripts\python.exe build.py imo_2025_n3 --final
```

Preview is 854×480 at 15 fps; final is 1920×1080 at 60 fps, both 16:9.
Use `--force` to rebuild despite the cache. A selected scene produces only
its clip; rerun the full build to reassemble the episode. Preview and final
caches are separate. Scene source, engine code, configuration, metadata,
Python version and Manim version form the fingerprint. Episode-level Python
helpers and SVG assets are included automatically. Changing one scene
invalidates that scene; changing the shared engine invalidates all scenes.
Keep episode-specific helper modules at the episode root so the renderer
includes them in `shared` and invalidates dependent scenes.

Build errors are reported with a log path and an excerpt. If external FFmpeg
is absent, the `imageio-ffmpeg` wheel supplies its executable. If neither is
available the build reports the missing dependency. Existing final videos
are replaced only after successful concatenation. Concat uses stream copy,
so clips must share the same profile. Only video streams are included.

## Files and architecture

- `engine/`: reusable theme, independent base scene, captions, equations,
  result boxes, problem chunks, case splits, contradiction marks, factor tokens,
  smooth transitions, fingerprinting and concatenation helpers.
- `config.py`: render profiles. `build.py`: ordered render orchestration.
- `episodes/imo_2025_n3/episode.yaml`: metadata and ordered module names.
- `episodes/imo_2025_n3/screenplay.md`: proof and visual instructions independent
  of Python. `scenes/`: one substantive scene per Python module.
- `episodes/imo_2025_n3/media/{preview,final}/`: Manim intermediate renders,
  cached LaTeX SVGs and cue timings for inspection.
- `episodes/imo_2025_n3/output/clips/{preview,final}/`: independent clips.
- `episodes/imo_2025_n3/output/imo_2025_n3_preview.mp4`: complete preview.
- `episodes/imo_2025_n3/output/imo_2025_n3_final.mp4`: complete final when rendered.
- `episodes/imo_2025_n3/output/*_preview.log`: per-scene diagnostics.

Generated media, videos and the venv are ignored by Git. There is no state
shared between Manim processes. Each module defines `EpisodeScene` and
recreates its opening visuals. Render a module directly from this directory:

```powershell
..\.venv\Scripts\python.exe -m manim -ql episodes/imo_2025_n3/scenes/scene_06_three_cases.py EpisodeScene
```

The video uses a centralized dark palette and LaTeX equations, with restrained
semantic accents. Text stays in short captions; equations transform between
steps. Case branches, divisor pairings, and prime token replacement add visual
explanation. `read()` checks presentation bounds and caption separation and
records cue times. Cue snapshots supplement those geometric checks.

## Verification

```powershell
..\.venv\Scripts\python.exe -m compileall -q engine episodes build.py config.py
..\.venv\Scripts\python.exe tools/verify_math.py
..\.venv\Scripts\python.exe tools/inspect_video.py imo_2025_n3 --preview
```

The math check enumerates actual divisors and compares survival against the
classification for all starting values through 10,000, checks the motivating
orbit, and tests the constructed family. This supports, and does not replace,
the written proof. Video inspection decodes each clip, verifies dimensions,
fps, absence of audio, and total duration, then creates contact sheets at all
recorded reading cues. It requires `ffprobe` from the external FFmpeg install.

## Creating the next video

1. Create `episodes/<new_id>/scenes/`.
2. Add the new problem and a human-readable `screenplay.md`. Validate the proof.
3. Add `episode.yaml` using the first episode's metadata and scene-order schema.
4. Ask an AI coding agent to generate one module per scene using `MathScene`
   and the existing engine components. Each module defines `EpisodeScene`.
5. Preview the episode, inspect contact sheets and motion, and edit individual
   scenes with `--scene`. Keep equations clear of the caption region.
6. Run the full preview build to reassemble the edited clips, then render final.

The screenplay-to-code step is manual/agent-assisted in v0.1. There is no
automatic screenplay parser. Extract a new reusable component only when the
episode needs a visual pattern the engine does not yet provide.
