# Local validation — 2026-10-04

## Completed checks

- Python syntax compilation passed for the engine, build system, tools and scenes.
- `pip check` reported no broken requirements in the local Python 3.12 venv.
- Manim Community 0.19.0 rendered all ten scenes in separate processes.
- Every scene passed the built-in frame-bounds and equation/caption separation checks.
- All 62 stable reading cues were exported and visually reviewed in contact sheets.
- The preview was concatenated into H.264/AVC MP4 with `yuv420p` pixel format.
- Preview: 854×480, 15 fps, 630.867 seconds (about 10 minutes 31 seconds).
- FFmpeg decoded every frame of each preview clip and the concatenated preview.
- FFprobe verified that each preview clip and the concatenated video contain exactly
  one video stream and no audio streams.
- The selected-scene command successfully located scene 6 without rebuilding it.
- After two scene edits, the incremental build rendered only scenes 5 and 7 and
  reused the other eight clips before reassembling the full preview.

## Final output

All ten scenes also rendered and concatenated at **1920×1080, 60 fps**.
The finished H.264/AVC `yuv420p` MP4 is **630.200 seconds** (10 minutes
30 seconds) and **21,897,349 bytes**. FFmpeg decoded every frame of all
ten final clips and the full final video without errors. FFprobe verified
the dimensions, frame rate, exactly one video stream and no audio streams.
The concatenated duration matches the sum of the ten clips.

All 62 final reading cues were exported; representative contact sheets were
also visually checked against the reviewed preview. Final reports and
contact sheets are in `episodes/imo_2025_n3/output/inspection_final/`.

Final artifact: `episodes/imo_2025_n3/output/imo_2025_n3_final.mp4`.

## Mathematical checks

`tools/verify_math.py` enumerates divisors independently of the scene code.
It verified the orbit 864 → 936 → 1014 → 1014 and compared the stated
classification with actual recurrence survival for all integers from 1 through
10,000. It also checked the constructed family for c = 0, …, 4 and every
positive m < 40 coprime to 10, including the exact number of growth steps.

The proof in `screenplay.md` supplies the general argument. Scene 9 includes
both necessity and constructive sufficiency, with the positive-integer
condition on m shown explicitly. Finite enumeration is supporting evidence,
not a replacement for that proof.

## Inspection artifacts

Generated reports, frames and contact sheets are in
`episodes/imo_2025_n3/output/inspection_preview/`. These and the generated
videos are local artifacts and excluded from Git. The inspection report is
reproducible with the command documented in README.
