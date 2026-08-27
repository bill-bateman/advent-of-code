from utils.filestuff import load_file

MOVES = {
    "^": (0, 1),
    "v": (0, -1),
    ">": (1, 0),
    "<": (-1, 0),
}


def part1(data: str) -> int:
    x, y = 0, 0
    visited = {(x, y)}

    for char in data:
        dx, dy = MOVES[char]
        x, y = x + dx, y + dy
        visited.add((x, y))

    return len(visited)


def part2(data: str) -> int:
    positions = [(0, 0), (0, 0)]
    visited = {(0, 0)}

    for i, char in enumerate(data):
        dx, dy = MOVES[char]
        x, y = positions[i % 2]
        positions[i % 2] = (x + dx, y + dy)
        visited.add(positions[i % 2])

    return len(visited)


def main():
    data = load_file(__file__, "3_real.txt")
    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
