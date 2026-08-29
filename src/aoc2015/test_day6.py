from aoc2015.day6 import part1, part2


def test_part1_basic():
    assert part1("turn on 0,0 through 999,999") == 1_000_000
    assert part1("turn off 0,0 through 999,999") == 0
    assert part1("toggle 0,0 through 999,0") == 1000
    assert part1("turn on 0,0 through 999,999\ntoggle 0,0 through 999,0") == 999_000
    assert (
        part1("turn on 0,0 through 999,999\nturn off 499,499 through 500,500")
        == 999_996
    )


def test_part2_basic():
    assert part2("turn on 0,0 through 0,0") == 1
    assert part2("toggle 0,0 through 999,999") == 2_000_000
    assert part2("turn off 0,0 through 0,0") == 0
    assert part2("toggle 0,0 through 0,0\nturn off 0,0 through 0,0") == 1
