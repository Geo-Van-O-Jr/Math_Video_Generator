# Approved design system · 1.0

The approved calibration is canonical: `episodes/imo_2017_p3/output/style_calibration.png` (1920 × 1080). SHA-256: `8b83ba5303e33d247195fe9e0bd1fc328e7ce148e97c85de16b6f3c54379f945`.

All new or revised scenes must import `engine/reference_theme.py` and `engine/components/reference_visuals.py`. Legacy scenes are not migrated by this static-only pass. Scene coordinates may encode mathematical composition; scenes must not introduce their own standard fonts, colors, glow strengths, stroke widths, dashes or box styles.

## Typography

Latin Modern Roman with matching LaTeX mathematics. Token sizes: title 64, subtitle 42, large body 46, body 43, small body 36, large mathematics 60, mathematics 54, labels 44, secondary note 27. Body minimum 36; label minimum 38. Never shrink prose to conceal overflow. Reflow explicit lines using `paragraph`; mathematical chunks stay intact.

## Color semantics

Gold identifies the rabbit and decisive conclusions; blue identifies the hunter and unit movement (including the rabbit's movement). Green/teal identifies reports, error bounds and the final distance/time goal. Pink and blue distinguish the two possible worlds. Primary, secondary and muted text are separate theme tokens. Semantic meaning overrides incidental color of a reference trail.

## Glow

Use `soft_glow`, `glow_dot`, `glow_line`, `glow_arrow`, `glow_icon`, `glow_box`. Point halos scale with point radius. Layer counts, widths and opacities are frozen in the theme or shared component implementation. Fade existing layered objects with `fade`; assigning one opacity to every halo layer destroys the approved falloff. Do not add blur/neon effects in scenes.

## Layout

16 × 9 canvas, 1920 × 1080 output. Horizontal safe margin .95, vertical .38, column gap .58; paragraph leading .57 and block gap .31. Use `LEFT_TEXT_COLUMN`, `RIGHT_DIAGRAM_COLUMN`, `check_bounds`, `enforce_safe_gap` and `no_overlap`. Standard prose column width is 7.2 units. Never move the title or rebuild the layout when a rule changes. Keep annotation labels separated from paths and point cores.

## Geometry

Stroke tokens: primary 2.35, secondary 1.55, auxiliary 1.15. Dash length .095 and duty ratio .49; circular geometry uses the shared dashed-circle helper. Use translucent regions at .09 opacity. Mathematical positions belong to anchor centers, not label/icon extents. Coincident characters use a blue core and concentric gold ring centered at precisely the same coordinate. Statement unit length is 1.25 design units consistently for both moves and the tracker disk. The approved two-worlds geometry retains its explicitly disclosed schematic scaling.

## Boxes

Use `glow_box` for results and `question_box` for the statement payoff. Shared corner radius .19, padding .34/.20, border and glow tokens. The statement question box is 10.6 × .94 at y=-3.62. Its border is subdued blue-gray and its goal phrase is teal. It enters only after the official final question reaches its conclusion; it is not persistent decoration. Gold is reserved for the two-worlds conclusion.

## Persistence / opacity hierarchy

Active 1.0, secondary .64, history .32, construction .28. Characters persist from the first sentence. At rule changes, retain geometry and reduce emphasis; do not replace the canvas. Prose is revealed in phrases, then retained, repositioned or selectively retired only after its meaning is carried by geometry. No whole-page fades. Final question quantities appear only at their textual cue.

## Regression gate

Before future component changes, preserve the canonical PNG and its hash. Render the calibration to a temporary media/output location with the same Cairo/LaTeX environment and compare decoded pixels; identical refactoring should yield identical pixels. Any intentional visual difference requires review against this approved board. Do not overwrite the baseline merely to make a check pass. Current pass preserves its original bytes and checks a fresh render against it. Main scene keyframes must also pass bounds checks and direct 1080p visual review.

Freeze validation: the fresh Cairo calibration render was pixel-identical to the approved PNG. The canonical PNG hash and existing MP4 hash remained unchanged. All eight corrected still states rendered at 1080p with bounds checks. Two-worlds auxiliary lines now leave label pockets around `Z=P_{200}` and `P_k`; font sizes and composition remain unchanged.
