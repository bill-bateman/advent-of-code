from aoc2015.day5 import is_nice, is_nice_v2, part1, part2


def test_is_nice_basic():
    assert is_nice("ugknbfddgicrmopn") is True
    assert is_nice("aaa") is True
    assert is_nice("jchzalrnumimnmhp") is False
    assert is_nice("haegwjzuvuyypxyu") is False
    assert is_nice("dvszwmarrgswjxmb") is False


def test_part1_basic():
    assert (
        part1("""ugknbfddgicrmopn
jchzalrnumimnmhp
aaa""")
        == 2
    )


def test_is_nice_v2_basic():
    assert is_nice_v2("qjhvhtzxzqqjkmpb") is True
    assert is_nice_v2("xxyxx") is True
    assert is_nice_v2("uurcxstgmygtbstg") is False
    assert is_nice_v2("ieodomkazucvgmuy") is False


def test_part2_basic():
    assert (
        part2("""qjhvhtzxzqqjkmpb
uurcxstgmygtbstg
xxyxx""")
        == 2
    )
