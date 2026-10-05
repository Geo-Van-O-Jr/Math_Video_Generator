# The hunter and the invisible rabbit

Silent English episode. Internal segment names below are production metadata and never appear in the video. The canvas has memory; every boundary is a held, exactly reconstructed mathematical state.

## Art direction

Use the four unmodified PNGs in `references/`. The sampled background is RGB (16,21,30). Computer Modern serif prose and LaTeX mathematics, ivory text, muted blue grey secondary facts, blue hunter, gold rabbit, green reports, pink/blue candidate routes. Thin dashed paths, translucent error disk and restrained vector halos. No scene numbers, subtitle strip, chapter cards, permanent headings, music or audio. The two-worlds reference supplies the palette and visual hierarchy; its incorrect distance-only tracker and circle geometry are replaced with the official straight-route construction.

## Opening and exact statement

About 12 seconds: “International Mathematical Olympiad”, then “Rio de Janeiro, 2017”, then “615 contestants.” The event title moves into “IMO 2017 · Problem 3”. No other historical claims.

The official English wording below is divided only for reading and layout. A miniature diagram grows beside it, in the official order rabbit → report → hunter. Each line is written over about two seconds, with additional reading holds. The full statement is never shown at once.

> A hunter and an invisible rabbit play a game in the Euclidean plane. The rabbit’s starting point, A₀, and the hunter’s starting point, B₀, are the same. After n−1 rounds of the game, the rabbit is at point Aₙ₋₁ and the hunter is at point Bₙ₋₁. In the nth round of the game, three things occur in order.
>
> (i) The rabbit moves invisibly to a point Aₙ such that the distance between Aₙ₋₁ and Aₙ is exactly 1.
>
> (ii) A tracking device reports a point Pₙ to the hunter. The only guarantee provided by the tracking device to the hunter is that the distance between Pₙ and Aₙ is at most 1.
>
> (iii) The hunter moves visibly to a point Bₙ such that the distance between Bₙ₋₁ and Bₙ is exactly 1.
>
> Is it always possible, no matter how the rabbit moves, and no matter what points are reported by the tracking device, for the hunter to choose her moves so that after 10⁹ rounds she can ensure that the distance between her and the rabbit is at most 100?

Keep the question beside the completed miniature geometry for 11 seconds. Then the same geometry expands into the canvas. Explicitly relabel “From here on: Rₙ=Aₙ, Hₙ=Bₙ.” This becomes “10⁹ rounds    HR≤100?” beneath the diagram. This is the first canonical segment boundary.

## Why growth is enough; a legal starting separation

The question becomes dₙ=HₙRₙ. Retain the hunter and rabbit, simplifying the obsolete rule apparatus into their joining segment. If dₙ>100, move the rabbit away by one unit, then let the hunter advance one unit. Write dₙ₊₁≥(dₙ+1)−1=dₙ. At exactly 100, one more block is needed. The aim is to force strict separation beyond 100.

Collapse the positions to O. “Fix any hunter strategy. Report P₁=O.” Grow the unit uncertainty disk. Show a faint arrow for the already determined first hunter move. “Choose the rabbit’s first move in the opposite direction.” Animate the rabbit first, then the hunter. Obtain d₁=2. This is a choice against a fixed strategy, not a retroactive rabbit move.

Reposition these same markers at Hₙ and Rₙ. Draw their line and label dₙ. “At the start of a block, reveal the rabbit’s exact position.” Emphasize Rₙ. “Even with this extra information, the hunter cannot win.” Fade those sentences while preserving the line, markers and distance. This is the second canonical boundary.

## The two indistinguishable routes — core motion test

“Two possible destinations. Each 200 units from Rₙ.” Construct RₙY₁, then physically reflect the first endpoint across HₙRₙ to construct Y₂. Mark perpendicular distances 1 on opposite sides. The schematic explicitly enlarges transverse distances and ε for visibility.

“Follow either straight route, one unit per round.” Two differently colored rabbit markers move together on their candidate paths. One green report moves along the central line; vertical connectors show its error relative to both candidates. Pause at four admissible common pings. The displayed motion interpolates between discrete rounds; the exact model and tests use integer k.

Write Pₖ=Rₙ+(k/200)(Z−Rₙ). Then |PₖR⁺ₙ₊ₖ|=|PₖR⁻ₙ₊ₖ|=k/200≤1. Both routes have exactly unit steps, and both generate the identical complete report sequence.

Only now write “Same information.” Then extend it to “Same information. Same hunter strategy.” Hold this reference composition. Keep the two candidate endpoints and routes for the minimax argument.

The hunter’s total path length is 200. Draw the straight path to H′. An arbitrary endpoint Q moves above the line, highlighting the longer connection to Y₂; then below the line, highlighting Y₁. A faint vertical boundary marks the maximum possible horizontal coordinate H′. “No reachable endpoint lies to the right of H′.” The active range 2≤dₙ≤100 makes Z strictly to its right, so these illustrations represent the exact minimax inequality in the source note.

Retain the pair of equal worst-case radii y. Introduce midpoint Z, the point R′ with RₙR′=200, and ε=ZR′. Show H′Z=dₙ−ε. “One of the two endpoints is at least y away.” This becomes the third canonical boundary. No whole-screen fade separates the geometry from its estimate.

## One continuous geometric estimate

The same diagram shrinks into the upper region, leaving room to write below. Pin 2≤dₙ<100 as the active assumption.

1. y²=1+(dₙ−ε)². Move this useful equation to a margin.
2. ε=200−√(200²−1). “The tiny loss in forward progress.”
3. Rationalize: ε=1/(200+√(200²−1))>1/400. Pin the strict bound.
4. From (200−ε)²=200²−1, transform to ε²+1=400ε. Pin this exact identity.
5. Return the remembered y equation to the writing position. Expand it to y²=dₙ²−2εdₙ+ε²+1, then substitute to obtain y²=dₙ²+ε(400−2dₙ).
6. Write 400−2dₙ>200. Emphasize this and ε>1/400 together. Transform the working equation into y²>dₙ²+1/2.
7. “At dₙ=100, the increment is still strictly greater than 1/2.” Extend the assumption to 2≤dₙ≤100. This covers the contest’s equality case.

The inequality becomes the blue highlighted fact d²ₙ₊₂₀₀>dₙ²+1/2. “A definite increase, every 200 rounds.” Keep the geometry above. This is the fourth canonical boundary.

## Count blocks, then rounds

Move the proved gain to the upper right. Transform the geometry into the reference-inspired left-side radial illustration: the same hunter, a faded old rabbit and dashed radius d, then a larger forced radius d_new. This illustration shows the change between block endpoints, not a monotonically increasing distance at every intermediate round.

Write Dⱼ=d₁₊₂₀₀ⱼ, D₀=2. Accumulate the retained fact into D²_N>4+N/2, valid until a block endpoint exceeds 100. At N=19,992, 4+N/2=10⁴, so the strict bound crosses distance 100. N≤19,992<2·10⁴.

Count the first round: T≤1+200·19,992. “Including the initial round.” Transform this into T<200·2·10⁴. The exact integer is 3,998,401, documented in mathematical QA.

Let 4,000,000 settle in a gold outline. Write 10⁹ to the right in blue; the < sign appears last. “Fewer than four million rounds suffice.” Hold the quantitative reference composition. No chapter heading or count appears.

Conclude d_T>100 ⇒ d_(10⁹)>100, by the already established move-away strategy. Transform this into the quiet mint-framed answer: “No. The hunter cannot guarantee a distance of at most 100.” Hold eight seconds. End on the proof, with no credits card or fade to black.

## Review and final rendering

The game and two-routes sequences are independently previewed before the algebra is built. The complete preview is then decoded and visually inspected, including all joins, reference keyframes and samples every eight seconds. Final 1080p/60 rendering waits for the preview approval explicitly required by the supplied prompt.

Source URLs, exact mathematical verification and corrections to the AI reference images are in [sources/README.md](sources/README.md).
