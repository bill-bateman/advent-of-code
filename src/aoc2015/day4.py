import hashlib

from utils.filestuff import load_file


def _mine(data: str, prefix: str) -> int:
    n = 1
    while True:
        if hashlib.md5(f"{data}{n}".encode()).hexdigest().startswith(prefix):
            return n
        n += 1


def part1(data: str) -> int:
    return _mine(data, "00000")


def part2(data: str) -> int:
    return _mine(data, "000000")


def main():
    data = load_file(__file__, "4_real.txt")
    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
