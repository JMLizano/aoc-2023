from typing import List, Tuple


def get_input(filepath: str):
    with open(filepath, "r") as f:
        return f.read().splitlines()


def tilt_north(rock_list: List[str]) -> List[Tuple[int, int]]:
    new_positions = []
    for i, line in enumerate(rock_list):
        for j, element in enumerate(line):
            if element == "O":
                rocks_in_column = 0
                for row in reversed(range(-1, i)):
                    if rock_list[row][j]  == "#":
                        rocks_in_column += 1
                        new_positions.append((row + rocks_in_column, j))
                        break
                    elif  row == -1:
                        new_positions.append((row + 1 + rocks_in_column, j))
                    elif rock_list[row][j]  == "O":
                        rocks_in_column += 1
                
    return new_positions

def get_value(num_rows: int, positions: List[Tuple[int, int]]) -> int:
    value = 0
    for (row, col) in positions:
        value += num_rows - row
    return value

if __name__ == '__main__':
    input = get_input("/Users/chema/personal/aoc-2023/day14/input16.txt")
    positions = tilt_north(input)
    print(positions)
    print(get_value(len(input), positions))