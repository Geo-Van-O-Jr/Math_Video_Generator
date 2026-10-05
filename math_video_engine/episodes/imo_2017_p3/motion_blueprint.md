# Motion blueprint — first two sequences only

Status: ready for animation implementation; no animation is implemented in this pass. Use the frozen `DESIGN_SYSTEM.md`. The static classes are inspection snapshots, not separate slides or animation scene boundaries.

## Grammar and timing

Keep a registry of persistent objects, with semantic IDs below. Construct each character once; subsequent beats transform that same object and its label. Build paths from mathematical anchors, never label bounding boxes. A snapshot factory may illustrate a target state but must not replace the entire animated diagram.

MICRO = 0.3–0.8 s for attention changes, point introduction or label updates. NORMAL = 0.8–1.8 s for a short phrase, segment or equation chunk. READ depends on the actual phrase length: initially budget spoken-word count at 2.2–2.8 words/s, add time for unfamiliar notation, then adjust to the eventual narration and reading review. This is a planning estimate, not final timing. HOLD = 0.8–2.0 s after a result. Avoid simultaneous competing reading and geometry changes; establish the noun, show its geometry, then allow reading to settle. Use grouped Write/FadeIn/LaggedStart, never character-by-character typewriter timing.

## A — official problem statement

Stable regions: title at the approved top-left position, exact official prose in the left column, the same two character anchors in the right column. Bottom box region remains empty until A8. No decorative unit heading or early billion-round label.

### Beats and cues

1. **A1 / opening — NORMAL + READ.** Introduce the title once. Reveal “A hunter and an invisible rabbit” as a phrase, then “play a game in the Euclidean plane.” At the first phrase, introduce both character marks together: blue center and gold concentric ring. Both centers are (4.2,.2). Gold emphasis belongs to “invisible rabbit.” Opening snapshot: `problem_statement_opening_rebuild.png`.
2. **A2 / coincidence — READ + NORMAL + HOLD.** Append the initial-condition sentence below the opening, preserving it. On “are the same,” write `A_0=B_0` above the existing coincident marks. Do not converge two different starting points: they already share a position. B/A labels sit on opposite sides, without changing their anchor coordinates. Snapshot: `problem_statement_initial_rebuild.png`.
3. **A3 / generic state — READ + NORMAL.** Append “After n−1 rounds…” below the existing sentences. Move the same hunter to (2.03,-1.16), rabbit to (5,.40); transform their labels to `B_{n-1}` and `A_{n-1}`. Morph the shared equality into these position labels rather than retaining a false equality. This transition summarizes earlier rounds, not a single unit move. Snapshot: `problem_statement_reference_rebuild.png`.
4. **A4 / ordered rules — NORMAL + READ.** Reveal the nth-round introduction. Make room using continuous upward movement within the left text viewport. Retire only already-read lines crossing its upper boundary after their content is embodied by the persistent anchors. Do not cross the title or erase a whole block simultaneously. Keep the generic-position sentence until rule (i) starts. No geometry resets.
5. **A5 / rabbit — READ, then NORMAL at “exactly 1.”** Reveal rule (i) in meaningful phrases. Preserve the hunter. At the exact unit cue, trace the blue radius-1 circle centered at `A_{n-1}` and the blue movement arrow. Move the gold rabbit along the straight segment to `A_n`; both start/end anchors are exactly 1 unit apart (1.25 screen units). Transform its position label; leave a dim starting marker. Do not trace a decorative curved path that suggests a different move. Snapshot: `problem_statement_rules_rebuild.png`.
6. **A6 / tracker — MICRO + READ + NORMAL.** Dim the rabbit-move group to history opacity .32, preserving its path and old anchor. As `P_n` is read, reveal the green report point and label. On “at most 1,” grow the green unit disk about `P_n`, then reveal the connector and bound `|P_nA_n|≤1`; the gold rabbit lies inside. Preserve the unmoved hunter. The unit label stays away from the tracker label and core. Snapshot: `problem_statement_tracking_rebuild.png`.
7. **A7 / hunter — MICRO + READ + NORMAL.** Keep tracker geometry at secondary opacity .64. Reveal rule (iii) below the retained end of rule (ii); retire only older lines as the viewport fills. On “exactly 1,” trace the blue circle centered at `B_{n-1}`, move the same hunter by the unit segment to `B_n`, and transform its label. Leave its starting marker as history. Rabbit remains at `A_n`. Snapshot: `problem_statement_hunter_rebuild.png`.
8. **A8 / question — READ + NORMAL + HOLD.** Continue the same text stream into the exact official question. At its `10^9` cue, reveal the teal quantity in prose and the diagram's rounds annotation. Until this cue, neither exists. Keep the last rule clause visible during the opening question phrase, then scroll it out individually. At “at most 100,” reveal the goal in teal and construct the bottom question box around its summary text; stroke first, phrase second, restrained glow last. Only now reach `problem_statement_question_rebuild.png`. Hold without removing the characters or accumulated geometry.

The approved large text cannot hold the whole official statement at once. A fixed, clipped text viewport implements a continuous reading stream: append phrases, shift existing lines together only when needed, and retire individual fully-read lines at the boundary. Preserve the last relevant clause across every rule transition. The static snapshots isolate the active text for inspection; do not implement their full paragraph replacement literally. No font shrinking or page-wide fades.

### Object lifecycle registry

| Object ID | ENTER | ACTIVE | PERSIST | DIM | TRANSFORM | EXIT |
|---|---|---|---|---|---|---|
| A.title | A1, one reveal | opening | entire A | never | none | only outside this sequence |
| A.prose.phrase.* | A1–A8 at exact wording cue | current phrase | until read and superseded | prior useful clause to secondary | upward viewport translation; semantic color only | individual off-viewport lines after meaning transfers to geometry |
| A.hunter | A1, blue core | A2, A3, A7 | every beat | no disappearance; retain legibility | common center → generic position → unit endpoint | none |
| A.rabbit | A1, gold ring | A2, A3, A5 | every beat | gold remains legible during tracker/hunter focus | ring fills into approved gold point as it separates; position changes only A3/A5 | none |
| A.position_labels | A1 B/A | each position cue | beside characters | secondary when another relation is read | equality → indexed positions → updated indices | equality retired through label transform at A3 |
| A.rabbit_move | A5 at unit cue | A5 | A6–A8 | .32 from A6 | trace path/circle, leave old marker | none |
| A.report | A6 at P_n | A6 | A7–A8 | .64 from A7 | reveal point then disk/bound; no arbitrary travel | none |
| A.hunter_move | A7 at unit cue | A7 | A8 | .32 in A8 | trace path/circle, retain starting marker | none |
| A.rounds | A8 at 10^9 | quantity cue | final state | none | reveal only | none |
| A.question | A8 at goal | final payoff | end of A | none | border → phrase → subtle glow | none |

## B — two indistinguishable worlds

Use the approved static target `two_worlds_reference_rebuild.png`. Its common axis is vertical: the candidates are LEFT and RIGHT. The prompt's suggested above/below construction is the same symmetry rotated; do not rotate the approved composition again. Retain pink left, blue right, the shared enlarged disk, and the scale note.

### Beats and cues

1. **B1 / inherited context — NORMAL + READ.** Reuse the existing `A_n`, `B_n` and axis from the preceding argument, placing them at (0,-.68), (0,-1.38) and x=0 if a handoff requires repositioning. Keep those identities; do not recreate them in a frame-wide fade. Reveal the two-worlds headline/subtitle once. A standalone future preview may initialize this context, explicitly treating it as inherited. No need to implement the intervening argument in this pass.
2. **B2 / Z — NORMAL.** Extend the common axis to Z=(0,1.22); reveal its white point and label `Z`. Show the schematic scale note before the stretched construction is read quantitatively.
3. **B3 / first candidate — NORMAL.** Trace the left unit radius from Z and introduce pink `Y_1` at (-4.25,1.22). Label the radius 1. The exaggerated transverse scale remains explicit.
4. **B4 / reflection — NORMAL + MICRO.** Transform a temporary copy of the first radius and endpoint through reflection about the vertical axis, reaching blue `Y_2` at (4.25,1.22). Keep the original pink endpoint. Label the second radius 1. The temporary copy becomes the second world, not an additional decorative ghost.
5. **B5 / routes — NORMAL + READ.** Trace the pink route from A_n to Y_1, then the blue reflected route; introduce each 200 label beside its own route. Retain both candidates and radii. These are the approved schematic straight routes, not curves copied from the generated reference.
6. **B6 / common reports — NORMAL per sample.** Introduce sample P_k points along the axis sequentially, e.g. k=50,100,150. On each cue briefly indicate both candidate positions at the same fraction k/200 of their respective routes. Add the matching horizontal error connector. Old sample dots remain secondary; the newest sample takes focus. Transform a single `P_k` label with the active sample; settle it in the approved final location. The report is one point shared by both possible worlds.
7. **B7 / error region — NORMAL.** Grow the shared final error disk about Z and transform the label to `Z=P_{200}`. Reveal its pink/blue fills gently behind all points and text. Never create two separate tracker disks or a distance-only observation.
8. **B8 / equation — NORMAL per chunk + READ.** Write `|P_k A_{n+k}^{(+)}|`, then `=`, then `|P_k A_{n+k}^{(-)}|`, then `=k/200`, finally `≤1`. Copy the corresponding label fragments from the highlighted diagram only where the same mathematical meaning is maintained. Do not morph arbitrary letters. Highlight the left connector for the first term, the reflected connector for the second, then both together for equality. Finish with the approved white equation; semantic flashes return to the base style.
9. **B9 / settle — MICRO + HOLD.** Dim crossbars to .28 and the axis to .64. Retain routes, endpoints, radii, report dots and labels. Retire the temporary moving sample-position markers because the routes and equation now encode their role; do not remove either possible world.
10. **B10 / same information — NORMAL.** Write the first conclusion phrase below the equation while the geometry remains still. Start the gold box border around the reserved final footprint.
11. **B11 / same strategy — NORMAL + HOLD.** Add “Same hunter strategy.” in gold, complete the border and restrained glow. Arrive at the exact approved target composition with ample hold. Do not begin the sequence with this result already visible.

### Object lifecycle registry

| Object ID | ENTER | ACTIVE | PERSIST | DIM | TRANSFORM | EXIT |
|---|---|---|---|---|---|---|
| B.hunter / B.rabbit | inherited at B1 | establishing configuration | entire B | no loss of identity | reposition only during handoff if necessary | none |
| B.axis | inherited at B1 | B2/B4/B6 | entire B | .64 after construction | extend toward Z | none |
| B.title / subtitle | B1 | opening | entire B | subtitle uses secondary color | none | none |
| B.Z | B2 | B2/B7 | entire B | none | label Z → Z=P_200 | none |
| B.Y1 / radius1 | B3 | first candidate | entire B | none | trace, then provide source for reflection | none |
| B.Y2 / radius2 | B4 reflected copy | symmetry | entire B | none | reflection and color shift to blue | none |
| B.routes / 200 labels | B5 | path construction | entire B | remain readable | progressive tracing | none |
| B.report_samples / P_k | B6, one at a time | current sample | old samples retained | previous samples secondary, final target opacities | label follows active report then settles | none |
| B.sample_positions | B6 on both routes | corresponding report | through equality explanation | secondary between samples | advance together at the same k | B9, once routes/equation preserve meaning |
| B.crossbars | each B6 sample | equal errors | final frame | .28 at B9 | extend from common report to both candidates | none |
| B.error_region | B7 | error bound | final frame | fixed translucent fill | grow behind geometry | none |
| B.equation.chunks | B8 in specified order | matching geometric relation | final frame | none | label copies where valid, then white final styling | none |
| B.conclusion | B10 first phrase, B11 second | final inference | final frame | none | complete gold emphasis/box | none |
| B.scale_note | B2 before stretched geometry | interpreting scale | final frame | secondary note color | none | none |

## First animation-pass acceptance gates

- No new style values, layouts, extra decoration or mathematical claims.
- Hunter/rabbit object IDs persist, and initial coordinates are exactly equal.
- No question box or billion-round quantity before its official cue.
- Movement blue, report bound green, character identities preserved.
- Review sampled transition frames as well as endpoints: no text/diagram collisions, clipped labels or transient out-of-bounds glow.
- Every equation chunk has time to be read; no per-word uniform timing.
- Preserve at least the immediately relevant prose clause during each rule transition.
- Reach the two-worlds target through construction, never a static frame reveal.
- Only these two sequences are eligible for the next pass; full episode and quantitative ending remain out of scope.
