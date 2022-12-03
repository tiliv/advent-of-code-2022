import functools
import itertools

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
priorities: dict[int, str] = dict(map(reversed, enumerate(alphabet, 1)))

def batched(iterable: list, size: int):
    it = iter(iterable)
    while (batch := list(itertools.islice(it, size))):
        yield batch

with open("data.txt") as f:
    assert 2641 == sum(map(priorities.get, [
        functools.reduce(set.intersection, map(set, group)).pop()
        for group in batched(map(str.strip, f.readlines()), size=3)
    ]))
