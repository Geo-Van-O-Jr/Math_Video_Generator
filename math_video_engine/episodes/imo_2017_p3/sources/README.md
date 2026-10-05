# Sources and mathematical editorial decisions

- Official contest statement, day 1, problem 3 (downloaded 2026-10-05): https://www.imo-official.org/assets/documents/problems/2017/2017_eng.pdf
- Official shortlist, C5, printed pages 44-45, PDF pages 46-47: https://www.imo-official.org/assets/documents/problems/2017/IMO2017SL.pdf
- Historical context (Rio de Janeiro, 615 contestants): https://www.imo-official.org/editions/2017/
- Requested rhythm reference: https://www.youtube.com/watch?v=uJqbHaFqjmI&t=3s . Unavailable to the web reader. The explicit motion rules in the supplied brief govern instead.

The statement in the film uses the official English wording and order; line breaks, mathematical typography and typographic apostrophes are the only layout changes. A_n/B_n are explicitly relabelled R_n/H_n before the proof. The tracker reports a **point within 1**, never the rabbit's distance. No score-distribution anecdote is used.

## Two small gaps that must not be imported into the film

The shortlist asks to keep the distance below 100. The contest statement asks for **at most** 100. Thus the film proves distance **strictly greater** than 100 and maintains that strict inequality. The block estimate also holds at d=100: epsilon>1/400 and 400-2d=200 still give a strict increment >1/2.

The H' minimax argument requires Z to the right of H'. It is not valid at the initial coincident position (nor for d<epsilon). To handle this rigorously, fix any hunter strategy, give the first ping at the common origin, and choose the rabbit's first unit vector opposite the hunter's resulting unit vector. This is a choice against a fixed strategy, not a reaction made after the hunter moves. It gives d_1=2 and an admissible ping at distance 1. At each later block endpoint distance increases, so d>=2>epsilon. Previous history may be revealed in full; the two new routes still have identical future reports.

With R=(0,0), H=(-d,0), set a=sqrt(39999), Y_+=(a,1), Y_-=(a,-1), Z=(a,0), R'=(200,0), H'=(200-d,0). At round k, both possible positions are (ka/200,+/-k/200); their common report is (ka/200,0). Consecutive rabbit positions have distance exactly 1. The report error is k/200<=1.

Any hunter endpoint Q=(u,v) has u<=200-d. Since a>200-d, the farther endpoint has squared distance (a-u)^2+(1+abs(v))^2 >= (a-(200-d))^2+1. This proves the minimax assertion for all reachable Q, not only the animated examples. The candidate route can be chosen in advance after computing the endpoint induced by the shared report sequence and fixed strategy.

Let epsilon=200-a=1/(200+a)>1/400. Squaring 200-epsilon=a gives epsilon^2+1=400epsilon. Thus y^2=1+(d-epsilon)^2=d^2+epsilon(400-2d)>d^2+1/2 for 2<=d<=100.

If a block endpoint exceeds 100, stop blocks and move radially away thereafter. Otherwise let D_j=d_(1+200j). Then D_j^2>4+j/2 for j>=1. At j=19,992, this is strictly greater than 10,000. So at most 19,992 blocks suffice, fewer than 20,000. Counting the first round, T<=1+200*19,992=3,998,401<4,000,000<10^9. This removes the otherwise unjustified strict fewer-than claim obtained merely by rounding 20,000 blocks.

The diagrams are schematic, with transverse separation and epsilon explicitly enlarged. Equal horizontal lengths R_nR'=H_nH'=200 are preserved in the layout. All numerical tests use true Euclidean coordinates, not display coordinates.
