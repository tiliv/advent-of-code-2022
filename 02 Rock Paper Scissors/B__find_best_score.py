import dataclasses
import pathlib
import typing

import pytest


SAMPLE, INPUT = (
    str((dir := pathlib.Path(__file__).parent) / "sample.txt"),
    str(dir / "data.txt"),
)
SOLUTIONS = dict("AY BZ CX".split())  # type: ignore
value = lambda mark: "ABCXYZ".index(mark) % 3
award = lambda m1, m2: 1 + value(m2) + 3 * [1, 2, 0][value(m2) - value(m1)]


def get_data(filename: str) -> typing.Iterator[list[str]]:
    with open(filename) as f:
        yield from (line.split() for line in f.readlines())


def solve(mark: str, strategy: str) -> str:
    """Rotate `mark` n times based on `strategy`."""
    for _ in range("YZX".index(strategy)):
        mark = "ABC"[value(SOLUTIONS[mark])]
    return mark


@dataclasses.dataclass
class TotalScoreResult:
    rounds: list[int]
    points: int

    def __repr__(self) -> str:
        return f"sum([ ... {len(self.rounds)} rounds ... ]) = {self.points}"

    @classmethod
    def get(cls, filename: str) -> typing.Self:  # type: ignore
        rounds: list[int] = [
            award(m1, solve(m1, strategy))
            for m1, strategy in get_data(filename)
        ]
        return cls(rounds, sum(rounds))


@pytest.mark.parametrize("filename, expected", [(SAMPLE, 12), (INPUT, 12683)])
def test(filename, expected):
    print(result := TotalScoreResult.get(filename))
    assert result.points == expected


if __name__ == '__main__':
    import subprocess
    subprocess.run(f"../.venv/bin/pytest '{__file__}'", shell=True)
