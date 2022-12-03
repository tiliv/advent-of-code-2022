import dataclasses
import enum
import pathlib
import typing

SOLUTIONS: dict[str, str] = dict("AY BZ CX".split())  # type: ignore


class Mark(enum.IntEnum):
    A = 1; B = 2; C = 3
    X = 1; Y = 2; Z = 3


class Award(enum.IntEnum):
    WIN = 6
    DRAW = 3
    LOSS = 0


def get_data() -> typing.Iterator[str]:
    with open(pathlib.Path(__file__).parent / 'data.txt') as f:
        yield from f.readlines()


def get_award(m1: str, m2: str) -> Award:
    if Mark[m1] == Mark[m2]:
        return Award.DRAW
    elif Mark[m2] == Mark[SOLUTIONS[m1]]:
        return Award.WIN
    return Award.LOSS


@dataclasses.dataclass
class TotalScoreResult:
    rounds: list[int]
    points: int

    def __repr__(self) -> str:
        return f"sum([ ... {len(self.rounds)} rounds ... ]) = {self.points}"

    @classmethod
    def get(cls) -> typing.Self:  # type: ignore
        iter_marks = (line.split() for line in get_data())
        rounds: list[int] = [
            Mark[m2].value + get_award(m1, m2).value
            for m1, m2 in iter_marks
        ]
        return cls(rounds, sum(rounds))


def test():
    print(result := TotalScoreResult.get())
    assert result.points == 12458


if __name__ == '__main__':
    print(TotalScoreResult.get())
