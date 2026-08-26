from aoc2015.day1 import part1

def test_basic():
	assert part1("()()") == 0
	assert part1(")())())") == -3