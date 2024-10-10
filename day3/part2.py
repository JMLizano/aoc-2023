from collections import defaultdict
from typing import Dict, List, Set, Tuple


def get_input(filepath: str):
    with open(filepath, "r") as f:
        return f.read().splitlines()


def gears_in_neighboorhood(row: int, col: int, engine_map: List[List[str]]) -> Set[Tuple[int, int]]:
    possible_gears = set()
    for row_modifier in [-1, 0, 1]:
        for col_modifier in [-1, 0, 1]:
            neighbor_row = min(max(row + row_modifier, 0), len(engine_map) -1)
            neighbor_col = min(max(col + col_modifier, 0), len(engine_map[0]) -1)
            neighbor = engine_map[neighbor_row][neighbor_col]
            if neighbor == "*":
                possible_gears.add((neighbor_row, neighbor_col))
    return possible_gears


def get_possible_gears(engine_map: List[List[str]]) -> Dict[Tuple[int, int], List[int]]:
    possible_gears_location = defaultdict(list)
    for row, character_line in enumerate(engine_map):
        current_number = ""
        current_gears_in_neighborhood = set()
        for col, character in enumerate(character_line):
            if character.isnumeric():
                current_number += character
                possible_gears_in_neighboorhood = gears_in_neighboorhood(row, col, engine_map)
                current_gears_in_neighborhood = current_gears_in_neighborhood.union(possible_gears_in_neighboorhood)
            if not character.isnumeric() or col == len(character_line) -1:
                if current_gears_in_neighborhood:
                    for gear_position in current_gears_in_neighborhood:
                        possible_gears_location[gear_position].append(int(current_number))
                current_number = ""
                current_gears_in_neighborhood = set()
    return possible_gears_location              


def get_valid_gear_value(possible_gears):
    total = 0
    for engine_parts_list in possible_gears.values():
        if len(engine_parts_list) == 2:
            total += engine_parts_list[0] * engine_parts_list[1]
    return total


if __name__ == '__main__':
    engine_map = get_input("input.txt")
    possible_gears = get_possible_gears(engine_map)
    print(get_valid_gear_value(possible_gears))
