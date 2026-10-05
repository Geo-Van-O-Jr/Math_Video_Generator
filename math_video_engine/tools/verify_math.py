"""Independent divisor enumeration checks for the episode's classification."""
from math import isqrt, gcd


def divisors(n):
    result = set()
    for d in range(1, isqrt(n) + 1):
        if n % d == 0:
            result.update((d, n // d))
    return sorted(result)


def next_term(n):
    ds = divisors(n)
    if len(ds) < 4:
        return None
    return sum(ds[-4:-1])


def survives(n):
    seen = set()
    for _ in range(300):
        if n in seen:
            return True
        seen.add(n)
        n = next_term(n)
        if n is None:
            return False
    raise AssertionError("Orbit unresolved; do not infer survival from a cutoff")


def classified(n):
    if n % 6:
        return False
    power = 0
    value = n
    while value % 2 == 0:
        power += 1
        value //= 2
    if power % 2 != 1:
        return False
    c = (power - 1) // 2
    base = 6 * 12 ** c
    return n % base == 0 and gcd(n // base, 10) == 1


if __name__ == "__main__":
    assert [next_term(n) for n in (864, 936, 1014)] == [936, 1014, 1014]
    for n in range(1, 10001):
        assert survives(n) == classified(n), n
    for c in range(5):
        for m in range(1, 40):
            if gcd(m, 10) != 1:
                continue
            n = 6 * 12 ** c * m
            for j in range(c):
                assert n == 6 * 12 ** (c-j) * 13 ** j * m
                n = next_term(n)
            assert next_term(n) == n == 6 * 13 ** c * m
    print("PASS: 10,000 initial values, example orbit, and constructive sufficiency.")
