import functools

alphabet = "abcdefghijklmnopqrstuvwxyz"
priorities: dict[str, int] = {
    **dict(map(reversed, enumerate(alphabet, 1))),  # type: ignore
    **dict(map(reversed, enumerate(alphabet.upper(), 27))),  # type: ignore
}

with open("data.txt") as f:
    assert 8401 == sum(
        priorities[common.pop()]  # type: ignore
        for line in f.readlines()
        if (n := len(line) // 2)
        if (common := functools.reduce(
            set.intersection,
            map(set, (line[:n], line[n:]))))  # type: ignore
    )
