import pytest

from aoc2015.day2 import extract_dimensions, part1, part2


def test_extract_dimensions_basic():

    assert extract_dimensions("1x2x3") == [1, 2, 3]
    with pytest.raises(ValueError):
        extract_dimensions("1x3x")
    with pytest.raises(ValueError):
        extract_dimensions("1x2")


def test_part1_basic():
    assert part1("2x3x4") == 58
    assert part1("1x1x10") == 43
    assert (
        part1("""2x3x4
1x1x10""")
        == 58 + 43
    )


def test_part2_basic():
    assert part2("2x3x4") == 34
    assert part2("1x1x10") == 14
    assert (
        part2("""2x3x4
1x1x10""")
        == 34 + 14
    )
