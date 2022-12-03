import functools

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
priorities: dict[int, str] = dict(map(reversed, enumerate(alphabet, 1)))

with open("data.txt") as f:
    lines = f.readlines()

assert 2641 == sum(map(priorities.get, [
    functools.reduce(
        set.intersection,
        map(set, map(str.strip, lines[i:i+3]))
    ).pop()
    for i in range(0, len(lines), 3)
]))
