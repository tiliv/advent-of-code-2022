import dataclasses
import functools
import pathlib
import pprint
import typing

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
priorities: dict[str, int] = dict(map(reversed, enumerate(alphabet, 1)))  # type: ignore

SAMPLE, INPUT = (
    str((dir := pathlib.Path(__file__).parent) / "sample.txt"),
    str(dir / "data.txt"),
)


def get_data(filename: str) -> typing.Iterator[str]:
    with open(filename) as f:
        yield from map(str.strip, f.readlines())


@dataclasses.dataclass
class PrioritiesResult:
    priorities: list[int]
    sum: int

    def __repr__(self) -> str:
        return f"sum({pprint.pformat(self.priorities)}) = {self.sum}"

    @classmethod
    def get(cls, filename: str) -> typing.Self:  # type: ignore
        lines = list(get_data(filename))
        letters: list[str] = [
            functools.reduce(set.intersection, map(set, group)).pop()  # type: ignore
            for i in range(0, len(lines), 3)
            if (group := lines[i:i+3])]
        values: list[int] = list(map(priorities.__getitem__, letters))
        return cls(values, sum(values))


def test():
    print(result := PrioritiesResult.get(SAMPLE))
    assert result.sum == 70

    print(result := PrioritiesResult.get(INPUT))
    assert result.sum == 2641


if __name__ == '__main__':
    test()
