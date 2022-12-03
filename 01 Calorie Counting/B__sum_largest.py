import dataclasses
import itertools
import pprint
import pathlib
import typing

import pytest

Inventory = list[int]
SAMPLE, INPUT = (
    str((dir := pathlib.Path(__file__).parent) / "sample.txt"),
    str(dir / "data.txt"),
)


def get_data(filename: str) -> str:
    """Return whole file as a stripped string."""
    with open(filename) as f:
        return f.read().strip()


def iter_inventories(data: str) -> typing.Iterator[Inventory]:
    """Split each separated grouping into a list of ints."""
    for group in data.split('\n\n'):
        yield [int(line) for line in group.split('\n')]


def find_largest_groups(groups: list[Inventory], n=3) -> list[Inventory]:
    """Return the `n` largest inventories by sum."""
    return sorted(groups, key=sum, reverse=True)[:n]


@dataclasses.dataclass
class LargestGroupsResult:
    groups: list[Inventory]
    sum: int

    def __repr__(self) -> str:
        return f"sum({pprint.pformat(self.groups)}) = {self.sum}"

    @classmethod
    def get(cls, filename: str) -> typing.Self:  # type: ignore
        data = get_data(filename)
        groups = list(iter_inventories(data))
        largest = list(find_largest_groups(groups))
        groups_sum = sum(itertools.chain(*largest))
        return cls(largest, groups_sum)


@pytest.mark.parametrize("filename, expected", [(SAMPLE, 45000), (INPUT, 209481)])
def test(filename, expected):
    print(result := LargestGroupsResult.get(filename))
    assert result.sum == expected


if __name__ == '__main__':
    import subprocess
    subprocess.run(f"../.venv/bin/pytest '{__file__}'", shell=True)
