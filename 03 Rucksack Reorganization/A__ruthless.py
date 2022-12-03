import functools

start, alphabet = 1, "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
priorities: dict[int, str] = {
    **dict(map(reversed, list(enumerate(alphabet.lower(), start)))),
    **dict(map(reversed, list(enumerate(alphabet, start + len(alphabet))))),
}

with open("data.txt") as f:
    print(sum(
        priorities[
            functools.reduce(
                set.intersection,
                map(set, (line[:n], line[n:]))
            ).pop()
        ]
        for line in f.readlines()
        if (n := len(line) // 2)
    ))
