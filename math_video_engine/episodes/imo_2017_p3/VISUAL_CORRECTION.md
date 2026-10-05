# Visual correction pass — delivered 2026-10-05

Scope: reusable visual system, calibration board, problem-statement stills and two-worlds still. No episode animation or quantitative ending was changed in this pass.

## Reusable system

`engine/reference_theme.py` centralizes semantic colors, Latin Modern prose/math typography, minimum font sizes, spacing, safe regions, line weights, dash rhythm, opacity and glow tokens. Titles use 64 pt, main statement prose 43 pt and mathematical labels 44 pt. Text is explicitly reflowed; overflow raises an error instead of silently shrinking type.

`engine/components/reference_visuals.py` provides serif/formula/paragraph builders, semantic emphasis, layered glow for points/lines/arrows/boxes/icons, dashed paths/circles, translucent uncertainty regions, two-column placement, bounds checks, separation checks and optional debug regions. Small points receive proportionally smaller halos. The system is opt-in so existing episode scenes retain their prior rendering until the visual baseline is accepted.

## Deliverables

All standalone renders are 1920 × 1080:

- `output/style_calibration.png`
- `output/problem_statement_reference_rebuild.png`
- `output/two_worlds_reference_rebuild.png`
- `output/problem_statement_rules_rebuild.png`
- `output/problem_statement_tracking_rebuild.png`
- `output/problem_statement_question_rebuild.png`

Side-by-side comparisons retain each image at 1920 × 1080 beneath a label band (3840 × 1140 total):

- `output/problem_statement_comparison.png`
- `output/two_worlds_comparison.png`

The corresponding `_comparison_display.png` derivatives are 1920 × 570 for reviewing both frames on a normal display.

## Review and limitations

All four authoritative reference images were inspected directly before style changes; the initial findings are in `VISUAL_AUDIT.md`. Calibration was rendered and visually revised before the statement, then the two-worlds composition. Final comparison images were inspected at display size. Render-time checks passed for registered safe bounds and intended gaps. Main text and diagrams are separated, with no counters or debug overlays.

The official statement is longer than the generated reference's paraphrase. Its full wording therefore occupies four still states at a consistent readable size. The primary export is the opening state, not the entire statement on one frame.

The two-worlds image preserves the pink/blue symmetry and gold conclusion but corrects the reference's distance-only tracker and separate-circle geometry. It shows a shared report region, symmetric 200-step routes and equal report errors. Transverse scale and the final disk are enlarged, explicitly identified in the image. This is a schematic, not an equal-scale geometric plot.

Latin Modern is compatible with the references but is not an exact recovered font match. Glow uses layered Cairo vector shapes rather than raster blur; background texture is deliberately subtle. These remain visual differences from the generated references.

## Reproduction

From `math_video_engine`, run with the existing virtual environment:

```powershell
../.venv/Scripts/python.exe tools/render_reference_still.py calibration
../.venv/Scripts/python.exe tools/render_reference_still.py problem
../.venv/Scripts/python.exe tools/render_reference_still.py problem-rules
../.venv/Scripts/python.exe tools/render_reference_still.py problem-tracking
../.venv/Scripts/python.exe tools/render_reference_still.py problem-question
../.venv/Scripts/python.exe tools/render_reference_still.py worlds
```

This helper calls Manim with `-s --format png`; it never invokes the episode build. Each run checks that existing output MP4 sizes and modification times remain unchanged.

The existing preview's SHA-256 was also confirmed unchanged after this pass:

`83cd39d5b2758b03ec90da9b6448a89e7ebb54a6aa28668914a24004ad30a206`

No full video was regenerated.
