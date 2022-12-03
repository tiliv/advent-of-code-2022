with open("data.txt") as f:
    assert 74711 == sorted(
        sum(map(int, group.split('\n')))
        for group in f.read().strip().split('\n\n')
    )[-1]
