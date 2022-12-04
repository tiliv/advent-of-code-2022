def has_overlap(pair) -> bool:
    r1, r2 = pair
    return (
        tuple(sorted((*r1, *r2))) not in ((*r1, *r2), (*r2, *r1))
        or r1[1] == r2[0]
        or r2[1] == r1[0])


with open("data.txt") as f:
    assert 867 == sum(
        int(has_overlap(
            tuple(map(int, range_info.split("-")))
            for range_info in line.strip().split(",")))
        for line in f.readlines()
    )
