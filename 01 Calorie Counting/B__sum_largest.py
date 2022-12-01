import dataclasses
import itertools
import pprint
import pathlib
import typing

Inventory = list[int]
INPUT_FILE = pathlib.Path(__file__).parent / 'data.txt'


def get_data() -> str:
    """Return whole file as a stripped string."""
    with open(INPUT_FILE) as f:
        return f.read().strip()


def iter_inventories(data: str) -> list[Inventory]:
    """Split each separated grouping into a list of ints."""
    for group in data.split('\n\n'):
        yield [int(line) for line in group.split('\n')]


def find_largest_groups(groups: list[Inventory], n=3) -> Inventory:
    """Return the `n` largest inventories by sum."""
    return sorted(groups, key=sum, reverse=True)[:n]


@dataclasses.dataclass
class LargestGroupsResult:
    groups: Inventory
    sum: int

    def __repr__(self) -> str:
        return f"sum({pprint.pformat(self.groups)}) = {self.sum}"

    @classmethod
    def get(cls) -> typing.Self:
        data = get_data()
        groups = list(iter_inventories(data))
        largest = list(find_largest_groups(groups))
        groups_sum = sum(itertools.chain(*largest))
        return cls(largest, groups_sum)


def test():
    print(result := LargestGroupsResult.get())
    assert result.sum == 209481


if __name__ == '__main__':
    print(LargestGroupsResult.get())
