import pytest
from aoc2015.day1 import part1, part2

def test_part1_basic():
	assert part1("()()") == 0
	assert part1(")())())") == -3

def test_part2_basic():
	assert part2(")") == 1
	assert part2("()())") == 5
	with pytest.raises(Exception):
		part2("()()")