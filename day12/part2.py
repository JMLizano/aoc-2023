
from typing import List
from itertools import combinations


def get_input(filepath: str):
    with open(filepath, "r") as f:
        return f.read().splitlines()


def get_combinations(unknowns: List[int], springs: List[int], groups: List[int]) -> List[List[int]]:
    to_place = sum(groups) - len(springs)
    possibilities = combinations(unknowns, to_place)
    return [sorted(list(pos) + springs) for pos in possibilities]


def evaluate(placement: List[int], groups: List[int]) -> bool:
    placement_groups = []
    current_group = 1
    for one, next in zip(placement[:-1], placement[1:]):
        if one + 1 == next:
            current_group += 1
        else:
            placement_groups.append(current_group)
            current_group = 1
    placement_groups.append(current_group)
    return placement_groups == groups

def get_indices_for_character(input_string: str, char: str) -> List[int]:
    indices = []
    for i, c in enumerate(input_string):
        if c == char:
            indices.append(i)
    return indices

def get_valid_combinations(springs, groups):
    unkowns = get_indices_for_character(springs, "?")
    springs = get_indices_for_character(springs, "#")
    groups = [int(c) for c in groups.split(",")]
    combs = get_combinations(unkowns, springs, groups)
    # print(combs, groups)
    valid = [comb for comb in combs if evaluate(comb, groups)]
    # print("VALID ", valid)
    return len(valid)

def run(input: str):
    combinations = 0
    for line in input:
        springs, groups = line.split()
        original_valid_combs = get_valid_combinations(springs, groups)
        expanded_left = get_valid_combinations("?" + springs, groups) if not springs.endswith("#") else original_valid_combs
        expanded_right = get_valid_combinations(springs + "?", groups) if not springs.startswith("#") else original_valid_combs
        expanded = max(expanded_left, expanded_right)
        # print("VALID ", valid)
        combinations += original_valid_combs * expanded ** 2
        # print("ORIGINAL ", original_valid_combs)
        # print("EXPANDED ", expanded)
        # print(original_valid_combs * expanded ** 4)
    return combinations


if __name__ == '__main__':
    input = get_input("/Users/chema/personal/aoc-2023/day12/input-test3.txt")
    print(run(input))