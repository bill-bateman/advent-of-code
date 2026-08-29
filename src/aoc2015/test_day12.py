from aoc2015.day12 import part1, part2, sum_all_numbers


def test_sum_all_numbers_basic():
    assert sum_all_numbers([1, 2, 3]) == 6
    assert sum_all_numbers({"a": 2, "b": 4}) == 6
    assert sum_all_numbers([[[3]]]) == 3
    assert sum_all_numbers({"a": {"b": 4}, "c": -1}) == 3
    assert sum_all_numbers([]) == 0
    assert sum_all_numbers({}) == 0


def test_sum_all_numbers_red_check():
    assert sum_all_numbers([1, 2, 3], do_red_check=True) == 6
    assert sum_all_numbers([1, {"c": "red", "b": 2}, 3], do_red_check=True) == 4
    assert (
        sum_all_numbers({"d": "red", "e": [1, 2, 3, 4], "f": 5}, do_red_check=True) == 0
    )
    assert sum_all_numbers([1, "red", 5], do_red_check=True) == 6


def test_part1_basic():
    assert part1("[1,2,3]") == 6


def test_part2_basic():
    assert part2('[1, {"c": "red", "b": 2}, 3]') == 4
