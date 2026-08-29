import re

import numpy as np

from utils.filestuff import load_file

INSTRUCTION = re.compile(r"(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)")


def _parse(line: str) -> tuple[str, tuple[slice, slice]]:
    match = INSTRUCTION.match(line)
    assert match, f"unparseable line: {line!r}"
    verb, x1, y1, x2, y2 = match.groups()
    x1, y1, x2, y2 = map(int, (x1, y1, x2, y2))
    return verb, (slice(x1, x2 + 1), slice(y1, y2 + 1))


def part1(data: str) -> int:
    grid = np.zeros((1000, 1000), dtype=bool)

    for line in data.splitlines():
        verb, sl = _parse(line)

        if verb == "turn on":
            grid[sl] = True
        elif verb == "turn off":
            grid[sl] = False
        else:
            grid[sl] ^= True

    return int(grid.sum())


def part2(data: str) -> int:
    grid = np.zeros((1000, 1000), dtype=int)

    for line in data.splitlines():
        verb, sl = _parse(line)

        if verb == "turn on":
            grid[sl] += 1
        elif verb == "turn off":
            grid[sl] = np.maximum(grid[sl] - 1, 0)
        else:
            grid[sl] += 2

    return int(grid.sum())


def main():
    data = load_file(__file__, "6_real.txt")
    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
