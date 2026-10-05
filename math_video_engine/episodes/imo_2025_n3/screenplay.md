# Which Starting Values Survive Forever?

IMO Shortlist 2025, Number Theory N3. Silent video; all presentation text is English.

## Actual problem statement

An infinite sequence a_1, a_2, ... consists of positive integers, each of
which has at least four positive divisors. For each n >= 1, a_{n+1} is the
sum of the three largest proper divisors of a_n. Determine all possible
values of a_1.

A proper divisor of a positive integer N is a divisor of N other than N.

## Direction and pacing

Reveal the statement in successive readable chunks. Keep captions near the
bottom, mathematics in the central region, and a chapter heading at the top.
Hold ordinary proof steps for about 6–9 seconds and difficult steps for
9–10 seconds, in addition to transition time. Every scene starts and ends
with a gentle fade; every scene can stand alone. Use matching equation
transforms, divisor-pair arrows, a three-way branching diagram, and animated
prime-token replacement. Mathematics is typeset with LaTeX throughout.

SCENE 1 — PROBLEM STATEMENT
------------------------------------------------------------

Show:

IMO Shortlist 2025
Number Theory — N3

Then reveal the statement progressively.

End with:

    Determine all possible values of a_1.

Then:

    Pause here if you'd like to solve it yourself.

Then transition into the solution.

------------------------------------------------------------
SCENE 2 — A CONCRETE EXPERIMENT
------------------------------------------------------------

Use 864 as the motivating example.

Show:

    864

Its three largest proper divisors:

    432, 288, 216

Animate:

    432 + 288 + 216 = 936

therefore:

    864 -> 936

Then similarly:

    936 -> 1014

Then:

    1014 -> 1014

Finish with:

    864 -> 936 -> 1014 -> 1014 -> ...

On-screen caption:

    "Some numbers grow for a while and then freeze."

Then:

    "Why?"

------------------------------------------------------------
SCENE 3 — TURN LARGE DIVISORS INTO SMALL DIVISORS
------------------------------------------------------------

Let:

    1 < p_1 < p_2 < p_3

be the three smallest divisors of a_n greater than 1.

Visually show divisor pairing:

    p  <---->  a_n / p

Explain visually that smaller divisors correspond to larger complementary
divisors.

Therefore the three largest proper divisors are:

    a_n/p_1,
    a_n/p_2,
    a_n/p_3.

Transform the recurrence into:

    a_{n+1}
      = a_n/p_1 + a_n/p_2 + a_n/p_3

then:

    a_{n+1}/a_n
      = 1/p_1 + 1/p_2 + 1/p_3.

Emphasize the threshold 1.

Caption:

    "Now everything depends on three reciprocals."

Then illustrate:

    ratio < 1  => shrinks
    ratio = 1  => freezes
    ratio > 1  => grows

------------------------------------------------------------
SCENE 4 — ODD TERMS ARE IMPOSSIBLE
------------------------------------------------------------

Assume a_n is odd.

Then:

    p_1 >= 3
    p_2 >= 5
    p_3 >= 7

Therefore:

    a_{n+1}/a_n
      <= 1/3 + 1/5 + 1/7
      = 71/105
      < 1.

Show visually that the ratio falls below 1.

Also explain:

all divisors involved are odd,
and odd + odd + odd is odd.

Therefore once the sequence becomes odd,
it remains odd and strictly decreases forever.

Display:

    a_n > a_{n+1} > a_{n+2} > ...

Then contradiction:

there is no infinite strictly decreasing sequence of positive integers.

Conclude:

    2 | a_n   for every n.

Display this as an important result.

------------------------------------------------------------
SCENE 5 — EVERY TERM MUST ALSO BE DIVISIBLE BY 3
------------------------------------------------------------

Now assume:

    2 | a_n
    but
    3 ∤ a_n.

Then:

    p_1 = 2,
    p_2 >= 4,
    p_3 >= 5.

Thus:

    a_{n+1}/a_n
       <= 1/2 + 1/4 + 1/5
       = 19/20
       < 1.

So such terms shrink.

We must show the sequence cannot escape by suddenly becoming divisible by 3.

Suppose for contradiction that:

    3 | a_{n+1}.

Because 3 ∤ a_n and none of p_1,p_2,p_3 are divisible by 3,
work modulo 3.

From:

    a_{n+1}
      = a_n(1/2 + 1/p_2 + 1/p_3),

we obtain:

    1/2 + 1/p_2 + 1/p_3 == 0 (mod 3).

Modulo 3:

    1^{-1} = 1
    2^{-1} = 2.

Hence:

    2 + p_2 + p_3 == 0 (mod 3).

The only possibility is:

    p_2 == p_3 == 2 (mod 3).

Now explain carefully:

If 4 divided a_n, then p_2 = 4,
but 4 == 1 (mod 3),
contradiction.

Therefore:

    4 ∤ a_n.

Since a_n is even:

    v_2(a_n) = 1.

Thus p_2 must be odd.

Also p_3 must be odd:
if p_3 were even, because v_2(a_n)=1 it would have the form 2d
with d an odd divisor of a_n.
Since p_3 is the third-smallest divisor greater than 1,
this forces d = p_2 and hence p_3 = 2p_2.
But if p_2 == 2 (mod 3), then:

    2p_2 == 1 (mod 3),

contradicting:

    p_3 == 2 (mod 3).

Therefore p_2 and p_3 are odd.

Now inspect:

    a_n/2      is odd,
    a_n/p_2    is even,
    a_n/p_3    is even.

So:

    a_{n+1}
      = odd + even + even
      = odd.

But odd terms were already proven impossible.

Contradiction.

Hence a valid infinite sequence cannot transition from
3 ∤ a_n to 3 | a_{n+1}.

So once a term lacks a factor 3, all later terms lack it
and strictly decrease.

Impossible.

Conclude prominently:

    6 | a_n   for every n.

This is the major turning point of the proof.

------------------------------------------------------------
SCENE 6 — ONLY THREE CASES REMAIN
------------------------------------------------------------

Since:

    6 | a_n,

the first two smallest divisors greater than 1 are:

    2 and 3.

Also 6 itself is a divisor.

Therefore the third-smallest divisor greater than 1 is one of:

    4, 5, 6.

Create a visual three-way case split.

CASE 4:

    1/2 + 1/3 + 1/4 = 13/12.

Therefore:

    a_{n+1} = (13/12)a_n.

Label:

    GROWTH.

CASE 5:

    1/2 + 1/3 + 1/5 = 31/30.

Therefore:

    a_{n+1} = (31/30)a_n.

Initially show that it also looks like growth.

CASE 6:

    1/2 + 1/3 + 1/6 = 1.

Therefore:

    a_{n+1} = a_n.

Label:

    FIXED POINT.

------------------------------------------------------------
SCENE 7 — CASE 5 IS A TRAP
------------------------------------------------------------

In the p_3 = 5 case:

    6 | a_n,
    5 | a_n,
    4 ∤ a_n.

Therefore:

    a_n = 30k

for some odd integer k.

Then:

    a_{n+1}
      = (31/30)(30k)
      = 31k.

Since k is odd:

    31k is odd.

But odd terms are impossible.

Visually eliminate the case p_3 = 5.

Only cases 4 and 6 remain.

------------------------------------------------------------
SCENE 8 — GROWTH CAN ONLY HAPPEN FINITELY MANY TIMES
------------------------------------------------------------

The only nonconstant transition is:

    a_{n+1} = (13/12)a_n.

Factor:

    12 = 2^2 * 3.

Use visual prime-factor tokens.

Show:

    2   2   3

being removed and replaced by:

    13.

In particular:

    v_2(a_{n+1})
       = v_2(a_n) - 2.

The number of factors 2 cannot decrease indefinitely.

Therefore the growth step can occur only finitely many times.

Eventually the sequence must enter the p_3 = 6 case
and become constant.

Show:

    13/12 -> 13/12 -> ... -> 1 -> 1 -> 1 -> ...

Caption:

    "Every surviving sequence eventually freezes."

------------------------------------------------------------
SCENE 9 — RECONSTRUCT ALL INITIAL VALUES
------------------------------------------------------------

Work backwards from the constant value.

In the fixed case:

    6 | A,
    4 ∤ A,
    5 ∤ A.

Hence:

    A = 6M,

where:

    M is odd
    and
    5 ∤ M.

Suppose there were exactly c growth steps.

Then:

    A
      = a_1 (13/12)^c.

So:

    a_1
      = A (12/13)^c.

For this to be an integer, A must contain at least c factors of 13.

Write:

    M = 13^c m.

Hence:

    A = 6 * 13^c * m.

Reversing c growth steps gives:

    a_1 = 6 * 12^c * m.

Since multiplication or division by powers of 13 does not affect
parity or divisibility by 5:

    m is odd,
    5 ∤ m.

Therefore:

    a_1 = 6 * 12^c * m,

where:

    c >= 0
    and
    gcd(m,10) = 1.

Then rewrite:

    6 * 12^c
      = 2^(2c+1) 3^(c+1).

So equivalently:

    a_1
      = 2^(2c+1) 3^(c+1) m,

with:

    c >= 0,
    gcd(m,10) = 1.

------------------------------------------------------------
Before leaving Scene 9, verify sufficiency explicitly:

For any c >= 0 and positive m with gcd(m,10) = 1, start with
a_1 = 6 * 12^c * m. After j growth steps, for 0 <= j <= c,

    a_{j+1} = 6 * 12^(c-j) * 13^j * m.

If j < c, the current term is divisible by 12, so its three smallest
divisors greater than 1 are 2, 3, 4. The next step multiplies it by 13/12.
At j = c, it equals 6 * 13^c * m. This term is not divisible by 4 or 5,
so its three smallest divisors greater than 1 are 2, 3, 6 and it stays fixed.
Every term is a multiple of 6 and hence has at least four positive divisors:
1, 2, 3, 6. This proves that every displayed starting value really works.
Keep the condition m > 0 visible with the classification.

------------------------------------------------------------
SCENE 10 — RETURN TO THE EXAMPLE AND CONCLUDE
------------------------------------------------------------

Return to:

    864.

Factor:

    864 = 6 * 12^2.

So c = 2 and m = 1.

Animate the two growth steps structurally:

    6 * 12^2
       ->
    6 * 12 * 13
       ->
    6 * 13^2.

Numerically:

    864 -> 936 -> 1014.

Now the number has only one factor 2,
so the growth case is no longer available.

It enters the fixed case:

    1014 -> 1014 -> 1014 -> ...

Finish with the classification:

    a_1 = 6 * 12^c * m

    c >= 0
    gcd(m,10) = 1.

Also show the equivalent form:

    a_1 = 2^(2c+1) 3^(c+1) m.

Final caption:

    "The sequence survives exactly when it has enough factors of 2 and 3
     to fuel finitely many growth steps, before reaching a fixed point."

Then fade out.
