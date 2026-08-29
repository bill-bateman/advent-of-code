from itertools import pairwise

from utils.filestuff import load_file

VOWELS = "aeiou"
BAD_PAIRS = ("ab", "cd", "pq", "xy")


def is_nice(line: str) -> bool:
    return (
        sum(c in VOWELS for c in line) >= 3
        and any(a == b for a, b in pairwise(line))
        and not any(bad in line for bad in BAD_PAIRS)
    )


def is_nice_v2(line: str) -> bool:
    first_seen = {}
    has_pair = False
    for i in range(len(line) - 1):
        pair = line[i : i + 2]

        if pair not in first_seen:
            first_seen[pair] = i
        elif i - first_seen[pair] >= 2:
            has_pair = True
            break

    has_split_repeat = any(line[i] == line[i + 2] for i in range(len(line) - 2))

    return has_pair and has_split_repeat


def part1(data: str) -> int:
    return sum(is_nice(line) for line in data.splitlines())


def part2(data: str) -> int:
    return sum(is_nice_v2(line) for line in data.splitlines())


def main():
    data = load_file(__file__, "5_real.txt")
    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
