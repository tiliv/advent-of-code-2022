with open("data.txt") as f:
    assert 209481 == sum(sorted(
        sum(map(int, group.split('\n')))
        for group in f.read().strip().split('\n\n')
    )[-3:])
