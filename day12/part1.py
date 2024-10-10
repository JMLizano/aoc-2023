
from typing import List
from itertools import combinations


def get_input(filepath: str):
    with open(filepath, "r") as f:
        return f.read().splitlines()


def get_combinations(unknowns: List[int], springs: List[int], groups: List[int]) -> List[List[int]]:
    to_place = sum(groups) - len(springs)
    possibilities = combinations(unknowns, to_place)
    pos = [sorted(list(pos) + springs) for pos in possibilities]
    print("POSSIBILITIES ", len(pos))
    return pos


def evaluate(placement: List[int], groups: List[int]) -> bool:
    placement_groups = []
    current_group = 1
    evaluated = 0
    for one, next in zip(placement[:-1], placement[1:]):
        if one + 1 == next:
            current_group += 1
        else:
            if current_group != groups[evaluated]:
                return False
            evaluated += 1
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

def run(input: str):
    combinations = 0
    for line in input:
        springs, groups = line.split()
        unkowns = get_indices_for_character(springs, "?")
        springs = get_indices_for_character(springs, "#")
        groups = [int(c) for c in groups.split(",")]
        combs = get_combinations(unkowns, springs, groups)
        # print(combs, groups)
        valid = [comb for comb in combs if evaluate(comb, groups)]
        print(len(valid))
        # print("VALID ", valid)
        combinations += len(valid)
    return combinations


if __name__ == '__main__':
    input = get_input("/Users/chema/personal/aoc-2023/day12/input-test4-expanded.txt")
    print(run(input))