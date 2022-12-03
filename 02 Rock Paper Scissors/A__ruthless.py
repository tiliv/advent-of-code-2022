value = lambda mark: "ABCXYZ".index(mark) % 3
award = lambda m1, m2: 1 + value(m2) + [3, 0, 6][value(m1) - value(m2)]

with open("data.txt") as f:
    assert 12458 == sum(award(*line.split()) for line in f.readlines())
