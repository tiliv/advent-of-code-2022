import itertools

with open("data.txt") as f:
    assert 573 == sum(
        int(tuple(sorted(parts)) in (
            (parts[0], *parts[2:], parts[1]),
            (parts[2], *parts[:2], parts[3]),
        ))
        for line in f.readlines()
        if (parts := tuple(itertools.chain.from_iterable([
            tuple(map(int, range_info.split("-")))
            for range_info in line.strip().split(",")
        ])))
    )
