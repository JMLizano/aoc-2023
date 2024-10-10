from functools import reduce
from typing import List


def get_input(filepath: str):
    with open(filepath, "r") as f:
        return f.read().splitlines()


def str_to_int_list(str_list: str) -> List[int]:
    return [int(e) for e in str_list.strip().split()]


def diff_between_elements(input_list: List[int]) -> List[int]:
    return [(input_list[i+1] - input_list[i]) for i in range(len(input_list) - 1)]


def derivate_until_zero(signal_series: List[int]) -> int:
    predicted_next_value = [signal_series[0]]
    derivated_series = signal_series
    while any(d != 0 for d in derivated_series):
        derivated_series = diff_between_elements(derivated_series)
        predicted_next_value.append(derivated_series[0])
    predicted_next_value.append(0)
    return reduce(lambda a,b: b - a,reversed(predicted_next_value))


def derivate_all_series(series_list: List[List[int]]) -> int:
    return sum(derivate_until_zero(series) for series in series_list)


if __name__ == '__main__':
    input = get_input("/Users/chema/personal/aoc-2023/day9/input.txt")
    input = [str_to_int_list(line) for line in input]
    print(derivate_all_series(input))