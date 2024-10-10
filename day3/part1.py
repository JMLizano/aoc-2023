

from typing import List


def get_input(filepath: str):
    with open(filepath, "r") as f:
        return f.read().splitlines()

def symbol_in_neighboorhood(row: int, col: int, engine_map: List[List[str]]) -> bool:
    for row_modifier in [-1, 0, 1]:
        for col_modifier in [-1, 0, 1]:
            neighbor_row = min(max(row + row_modifier, 0), len(engine_map) -1)
            neighbor_col = min(max(col + col_modifier, 0), len(engine_map[0]) -1)
            neighbor = engine_map[neighbor_row][neighbor_col]
            if not neighbor.isnumeric() and neighbor != ".":
                return True
    return False

def get_engine_parts(engine_map: List[List[str]]) -> List[int]:
    engine_parts = []
    for row, character_line in enumerate(engine_map):
        current_number = ""
        is_engine_part = False
        for col, character in enumerate(character_line):
            if character.isnumeric():
                current_number += character
                is_engine_part = is_engine_part or symbol_in_neighboorhood(row, col, engine_map)
            if not character.isnumeric() or col == len(character_line) -1:
                if is_engine_part:
                    engine_parts.append(int(current_number))
                current_number = ""
                is_engine_part = False
    return engine_parts              

if __name__ == '__main__':
    engine_map = get_input("input.txt")
    engine_parts = get_engine_parts(engine_map)
    print(sum(engine_parts))
