import dataclasses
import itertools
import pathlib
import typing

INPUT_FILE, SAMPLE_FILE = (
    str((dir := pathlib.Path(__file__).parent) / "data.txt"),
    str(dir / "sample_data.txt"),
)
value = lambda mark: "ABCXYZ".index(mark) % 3
award = lambda m1, m2: 1 + value(m2) + [3, 0, 6][value(m1) - value(m2)]


def get_data(filename: str = INPUT_FILE) -> typing.Iterator[list[str]]:
    with open(filename) as f:
        yield from (line.split() for line in f.readlines())


@dataclasses.dataclass
class TotalScoreResult:
    rounds: list[int]
    points: int

    def __repr__(self) -> str:
        return f"sum([ ... {len(self.rounds)} rounds ... ]) = {self.points}"

    @classmethod
    def get(cls, filename: str) -> typing.Self:  # type: ignore
        rounds: list[int] = list(itertools.starmap(award, get_data(filename)))
        return cls(rounds, sum(rounds))


def test():
    print(result := TotalScoreResult.get(SAMPLE_FILE))
    assert result.points == 15

    print(result := TotalScoreResult.get(INPUT_FILE))
    assert result.points == 12458


if __name__ == '__main__':
    print(TotalScoreResult.get(INPUT_FILE))
