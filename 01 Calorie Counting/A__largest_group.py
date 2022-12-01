import dataclasses
import pprint
import pathlib
import typing

Inventory = list[int]
INPUT_FILE = pathlib.Path(__file__).parent / 'data.txt'


def get_data() -> str:
    """Return whole file as a stripped string."""
    with open(INPUT_FILE) as f:
        return f.read().strip()


def iter_inventories(data: str) -> typing.Iterator[Inventory]:
    """Split each separated grouping into a list of ints."""
    for group in data.split('\n\n'):
        yield [int(line) for line in group.split('\n')]


def find_largest_group(groups: list[Inventory]) -> Inventory:
    """Return the largest inventory by sum."""
    return sorted(groups, key=sum, reverse=True)[0]


@dataclasses.dataclass
class LargestGroupResult:
    group: Inventory
    sum: int

    def __repr__(self) -> str:
        return f"sum({pprint.pformat(self.group)}) = {self.sum}"

    @classmethod
    def get(cls) -> typing.Self:  # type: ignore
        data = get_data()
        groups = list(iter_inventories(data))
        group = find_largest_group(groups)
        return cls(group, sum(group))


def test():
    print(result := LargestGroupResult.get())
    assert result.sum == 74711


if __name__ == '__main__':
    print(LargestGroupResult.get())
