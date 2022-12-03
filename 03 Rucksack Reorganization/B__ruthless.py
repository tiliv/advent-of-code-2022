import functools

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

with open("data.txt") as f:
    lines = f.readlines()

assert 2641 == sum([
    1 + alphabet.index(functools.reduce(set.intersection, sets).pop())  # type: ignore
    for i in range(0, len(lines), 3)
    if (sets := map(set, map(str.strip, lines[i:i+3])))  # type: ignore
])
