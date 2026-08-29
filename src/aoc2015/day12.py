import json

from utils.filestuff import load_file


def sum_all_numbers(json_obj, do_red_check=False) -> int:
    if isinstance(json_obj, dict):
        # red check
        if do_red_check and any(
            isinstance(value, str) and value == "red" for value in json_obj.values()
        ):
            return 0

        return sum(
            [sum_all_numbers(value, do_red_check) for value in json_obj.values()]
        )
    if isinstance(json_obj, list):
        return sum([sum_all_numbers(value, do_red_check) for value in json_obj])
    if isinstance(json_obj, int):
        return json_obj
    return 0


def part1(data: str) -> int:
    obj = json.loads(data)
    return sum_all_numbers(obj)


def part2(data: str) -> int:
    obj = json.loads(data)
    return sum_all_numbers(obj, do_red_check=True)


def main():
    data = load_file(__file__, "12_real.txt")
    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
