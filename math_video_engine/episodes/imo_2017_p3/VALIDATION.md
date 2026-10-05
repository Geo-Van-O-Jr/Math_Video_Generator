# Preview validation — 2026-10-05

Status: complete preview rendered and inspected; final 1080p/60 render intentionally pending user approval, as requested in the supplied production prompt. No approval has been recorded.

## Reviewable deliverables

- [Review page with video and reference comparisons](output/review.html)
- [Complete silent preview](output/imo_2017_p3_preview.mp4)
- [Screenplay](screenplay.md)
- [Exact sources and proof details](sources/README.md)
- [Machine-readable inspection report](output/inspection_preview/report.json)
- Five independent clips in `output/clips/preview/`.
- Four unchanged reference PNGs in `references/`, verified byte-for-byte against the supplied originals using SHA-256.
- Four native-resolution extracted keyframes and four side-by-side comparisons in `output/inspection_preview/`.
- Five uniform eight-second contact sheets and four semantic-cue contact sheets in that inspection directory.

## Technical checks

- Complete duration: **479.133333 seconds (7 min 59 s)**.
- Preview: **854 × 480**, **15 fps**, H.264 MP4, one video stream, **zero audio streams**.
- All frames in every clip and the concatenated video decoded successfully with FFmpeg error checking.
- 44 semantic reading cues checked; presentation bounds checked during rendering.
- Python compilation passed for engine, episode, renderer and tools.
- The complete-build manifest, source fingerprints, clip caches and video SHA-256 agree. The inspector refuses stale source/clip combinations.
- Final-render approval gate tested without an approval flag: rejected before rendering, with the expected “requires user preview approval” message.

## Continuity and visual review

Inspected the two-routes pilot before implementing the algebra, then reviewed its revised colors, label spacing and explicit definitions. The frame sequence shows a first route, its actual reflected counterpart, moving paired rabbits and common pings, then the endpoint minimax construction. Removing those movements would remove the explanation of shared information and worst-case geometry.

Inspected all five eight-second contact sheets, the four reference comparisons, and both sides of every internal boundary. Objects persist through changes of focus; there are no chapter cards, numbered headings, progress bars, permanent subtitles, or black inter-segment resets. Reading pauses are deliberate in a silent mathematical film.

Mean absolute RGB differences across the four segment joins, on the 0–255 scale:

| Boundary | Mean difference |
| --- | ---: |
| Game → strategy | 0.2505 |
| Strategy → routes | 0.0159 |
| Routes → estimate | 0.2757 |
| Estimate → conclusion | 0.3222 |

The same canonical constructors reproduce geometry, colors and framing. The decoded compressed frames are not claimed to be pixel-identical; before/after sheets and amplified differences are included for inspection. No visible reset or black flash was found in the reviewed joins.

The references are art direction, not mathematical diagrams to copy literally. The film preserves navy/serif/vector styling, semantic color, dashed geometry, uncertainty fill and outlined result highlights. It replaces the incorrect distance-only tracker and incorrect symmetric-circle geometry with the official 200-round construction. It also replaces the incorrect numerical conclusion. It deliberately uses sparser accumulated prose and removes all slide chrome. Preview rasterization is softer than the requested final 1080p render.

## Mathematical checks

`python tools/verify_hunter_rabbit.py` passed:

- epsilon identities and strict bound, checked with 60-digit arithmetic;
- all 200 unit steps and their compatible common reports;
- 25,000 sampled reachable hunter endpoints checked against the analytic minimax bound;
- the endpoint case d=100;
- the legal first-round separation d₁=2;
- exact accounting: at most 19,992 blocks after the first round, hence at most 3,998,401 rounds, strictly fewer than 4,000,000 and 10⁹.

The numerical checks support the exact geometric proof in `sources/README.md`; they do not replace it. The official statement is preserved in English, with A/B explicitly renamed R/H for the proof. No unverified score-distribution or medallist anecdote appears.

## Reference keyframe positions in the concatenated preview

| Composition | Timestamp |
| --- | --- |
| Official question / statement composition | 1:42.50 |
| Basic game geometry | 2:00.83 |
| Two indistinguishable routes | 4:03.03 |
| Four-million / billion comparison | 7:39.00 |

## Next authorized stage

After the user approves this concrete preview:

```powershell
..\.venv\Scripts\python.exe build.py imo_2017_p3 --final --approve-preview
..\.venv\Scripts\python.exe tools/inspect_video.py imo_2017_p3 --final
```

Run from `math_video_engine`. Final resolution is 1920 × 1080 at 60 fps. A change to rendering sources or to the inspected preview invalidates approval.
