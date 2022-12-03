import functools

start, alphabet = 1, "abcdefghijklmnopqrstuvwxyz"
priorities: dict[int, str] = {
    **dict(map(reversed, enumerate(alphabet, 1))),
    **dict(map(reversed, enumerate(alphabet.upper(), 27))),
}

with open("data.txt") as f:
    assert 8401 == sum(
        priorities[common.pop()]
        for line in f.readlines()
        if (n := len(line) // 2)
        if (common := functools.reduce(
            set.intersection,
            map(set, (line[:n], line[n:]))))
    )
