# Visual correction audit — before changing the style system

Directly inspected all four files in `references/`, the previous problem and two-worlds keyframes, `engine/theme.py`, `living_canvas.py`, `text_blocks.py`, episode `visuals.py`, the SVGs and rendering configuration.

## Root causes

- The old 27–32 pt body/labels and 40 pt opening title were materially smaller than the references. Additional `.47`, `.63`, `.72` scaling made important labels especially weak. The references devote much more screen area to typography.
- `prose`, `math` and `fit` silently scaled overflowing text. That hid layout errors and destroyed a consistent hierarchy. New typography must reject undersized layouts and reflow explicitly.
- The serif family itself was directionally compatible, but the small scale, default weight and lack of bold semantic phrases made it feel like raw TeX. The original Segoe UI theme also remained a competing system.
- The statement was all white. Invisible rabbit, unit motion and the distance goal did not carry the gold/blue/mint semantic emphasis seen in the reference.
- A single 8-pixel, 5.5%-opacity duplicate was not an effective glow. Dots were tiny and uniformly filled. Reference points have a luminous core, colored rim and a broad, soft falloff; boxes have a crisp border plus restrained glow.
- The flat background and barely visible fills removed depth. The reference has a very subtle navy vignette, translucent regions, strong active objects and quieter history.
- Layouts used unrelated coordinates rather than explicit regions. The right vignette was too small; line widths and label placement were inconsistent. Bounds checks did not detect text/diagram conflicts.
- The old two-worlds composition was an elongated textbook triangle with all of its visual weight at the right. It lost the reference's centered symmetry, large endpoint labels, strong equation and gold conclusion box.

## Measured design direction

Reference size: 1672 × 941 (approximately 16:9). Reference statement left margin ≈6%; title top ≈4%; left text spans ≈45% of width; the vignette occupies the right ≈43%; bottom question box spans ≈62%. Main body cap height is approximately 40–48 reference pixels, not the previous small reconstruction. The two-worlds title is about 6% of frame height, its main diagram about 43%, and the full-width conclusion about 10%.

Use a 16 × 9 design canvas rendered to 1920 × 1080 PNG. Centralize type, line leading, margins, semantic colors, stroke widths, dashes, glow strength, point sizes, region opacity and box geometry. Keep native Computer Modern / LaTeX-compatible serif typography, at a substantially larger, enforced scale, with bold colored phrases.

## Scope and fidelity decisions

Only a calibration board, problem reference still states, and a two-worlds still are being built. Existing episode scene files and MP4s will remain unchanged; no full-episode renderer will be invoked.

The complete official statement cannot occupy the reference's left column at its large type size: it is longer than the generated paraphrase. Use several still reveal states with the exact official wording and one visually representative primary export. The bottom question box is a clearly supplementary summary, not a replacement for the exact question.

For the two-worlds frame, rotate the correct 200-round construction so the two candidate endpoints sit symmetrically to the left and right of a central axis. The common reports stay on that axis. A shared unit-error disk at the final report supplies the reference's dashed translucent geometry. Do not copy the false distance-only tracker or the two incorrect separate circles. Mark the drawing as schematic without making main labels tiny.
