import functools

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
priorities: dict[int, str] = dict(map(reversed, enumerate(alphabet, 1)))  # type: ignore

with open("data.txt") as f:
    lines = f.readlines()

assert 2641 == sum(map(priorities.get, [  # type: ignore
    functools.reduce(
        set.intersection,
        map(set, map(str.strip, lines[i:i+3]))  # type: ignore
    ).pop()
    for i in range(0, len(lines), 3)
]))
