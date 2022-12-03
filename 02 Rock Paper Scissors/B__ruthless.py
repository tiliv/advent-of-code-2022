value = lambda mark: "ABCXYZ".index(mark) % 3
award = lambda m1, m2: 1 + value(m2) + [3, 0, 6][value(m1) - value(m2)]

def solve(mark: str, strategy: str) -> str:
    """Rotate `mark` n times based on `strategy`."""
    for _ in range("YZX".index(strategy)):
        mark = "ABC"[value(dict("AY BZ CX".split())[mark])]  # type: ignore
    return mark

with open("data.txt") as f:
    assert 12683 == sum(
        award(m1, solve(m1, strategy))
        for m1, strategy in (line.split() for line in f.readlines())
    )
