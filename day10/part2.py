
from typing import List, Tuple


def get_input(filepath: str):
    with open(filepath, "r") as f:
        return f.read().splitlines()


def find_starting_point(input: List[str]) -> Tuple[int, int]:
    for i, line in enumerate(input):
        j = line.find("S")
        if j != -1:
            return i, j


def find_initial_pipe_directions(starting_point: Tuple[int, int], pipe_map: List[str]):
    row, col = starting_point
    pipe_directions = []
    # North neighbor
    if pipe_map[row - 1][col] in ["|", "7", "F"]:
        pipe_directions.append((-1, 0))
    # east neighbor
    if pipe_map[row][col + 1] in ["-", "J", "7"]:
        pipe_directions.append((0, 1))
    # South neighbor
    if pipe_map[row + 1][col] in ["|", "J", "L"]:
        pipe_directions.append((1, 0))
    # West neighbor
    if pipe_map[row][col - 1] in ["-", "F", "L"]:
        pipe_directions.append((0, -1))
    return pipe_directions


def get_next_position(current_position: Tuple[int, int], direction: str) -> Tuple[int, int]:
    return (current_position[0] + direction[0], current_position[1] + direction[1])


def update_direction(previous_direction: Tuple[int, int], pipe: str) -> Tuple[int, int]:
    if pipe == "L":
        return (previous_direction[1], previous_direction[0])
    if pipe == "7":
        return (previous_direction[1], previous_direction[0])
    if pipe == "F":
        return (-previous_direction[1], -previous_direction[0])
    if pipe == "J":
        return (-previous_direction[1], -previous_direction[0])
    return previous_direction


def get_left_position(current_position: Tuple[int, int], direction: str) -> Tuple[int, int]:
    # North - (-1, 0) -> west (0, -1)
    # east - (0, 1) -> north (-1, 0)
    # South - (-1, 0) -> east (0, 1)
    # West - (0, -1) -> south (1, 0)
    left_direction = [-direction[1], direction[0]]
    return get_next_position(current_position, left_direction)


def get_right_position(current_position: Tuple[int, int], direction: str) -> Tuple[int, int]:
    # North - (-1, 0) -> east (0, 1)
    # east - (0, 1) -> south (1, 0)
    # South - (1, 0) -> west (0, -1)
    # West - (0, -1) -> north (-1, 0) 
    right_direction = [direction[1], -direction[0]]
    return get_next_position(current_position, right_direction)


def mark_pipe_sides(
    starting_point: Tuple[int, int],
    initial_direction: str,
    pipe_map: List[str]
) -> Tuple[List[Tuple[int, int]], List[Tuple[int, int]], List[Tuple[int, int]]]:
    (x, y) = get_next_position(starting_point, initial_direction)
    direction = update_direction(initial_direction, pipe_map[x][y])
    left_side = [get_left_position((x, y), initial_direction)]
    pipe = [(x, y)]
    right_side = [get_right_position((x, y), initial_direction)]
    while (x, y) != starting_point:
        (x, y)  = get_next_position((x, y), direction)
        direction = update_direction(direction, pipe_map[x][y])
        left_side.append(get_left_position((x,y), direction))
        pipe.append((x,y))
        right_side.append(get_right_position((x,y), direction))
    return left_side, pipe, right_side


def identify_inner_side(left_side: List[Tuple[int, int]], right_side: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    left_min_x = min(left_side, key=lambda x: x[0])
    right_min_x = min(right_side, key=lambda x: x[0])
    if left_min_x < right_min_x:
        print('Right side is inner')
        return right_side
    elif left_min_x > right_min_x:
        print('Left side is inner')
        return left_side
    else:
        print('What?! Both sides share the same tiles?')


def clean_inner_positions(inner_side: List[Tuple[int, int]], pipe: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    return list(set([p for p in inner_side if p not in pipe]))


def expand_inner_space(inner_positions: List[Tuple[int, int]], pipe: List[Tuple[int, int]]) -> int:
    visited = []
    to_expand = inner_positions
    while len(to_expand) > 0:
        position = to_expand.pop(0)
        visited.append(position)
        for neighbor_direction in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            nx, ny = get_next_position(position, neighbor_direction)
            if (nx, ny) not in visited and (nx, ny) not in to_expand and (nx, ny) not in pipe:
                to_expand.append((nx, ny))
    return visited

def print_pipes(inner_space, pipes, input):
    to_print = ""
    for x, line in enumerate(input):
        for y, character in enumerate(line):
            if (x,y) in inner_space:
                to_print += "X"
            elif (x, y) in pipe:
                to_print += character
            else:
                to_print += "."
        to_print += "\n"
    print(to_print)

if __name__ == '__main__':
    pipe_map = get_input("input.txt")
    starting_point = find_starting_point(pipe_map)
    initial_direction_1, initial_direction_2 = find_initial_pipe_directions(starting_point, pipe_map)
    inner_space = []
    for initial_direction in [initial_direction_2, initial_direction_1]:
        left_side, pipe, right_side = mark_pipe_sides(starting_point, initial_direction, pipe_map)
        inner_side = identify_inner_side(left_side, right_side)
        inner_positions = clean_inner_positions(inner_side, pipe)
        inner_space += expand_inner_space(inner_positions, pipe)
        # print_pipes(inner_space, pipe, pipe_map)
    print(len(set(inner_space)))
