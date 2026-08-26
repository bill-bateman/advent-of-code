from utils.filestuff import load_file


def extract_dimensions(line: str) -> list[int]:
    dims = [int(s) for s in line.split("x")]
    if len(dims) != 3:
        raise ValueError(
            "dims should have length 3, but has length % (dims: %)", len(dims), dims
        )
    return dims


def part1(data: str) -> int:
    total = 0

    for line in data.splitlines():
        dims = extract_dimensions(line)

        areas = [
            dims[0] * dims[1],
            dims[0] * dims[2],
            dims[1] * dims[2],
        ]
        total += min(areas) + 2 * sum(areas)

    return total


def part2(data: str) -> int:
    total = 0

    for line in data.splitlines():
        dims = extract_dimensions(line)

        dims.sort()  # ascending
        wrap = 2 * (dims[0] + dims[1])
        bow = dims[0] * dims[1] * dims[2]
        total += wrap + bow

    return total


def main():
    data = load_file(__file__, "2_real.txt")
    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
