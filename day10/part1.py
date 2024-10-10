
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


def move_through_pipe(
        starting_point: Tuple[int, int],
        initial_directions: List[str],
        pipe_map: List[str]
) -> int:
    steps = 1
    (x_a, y_a), (x_b, y_b) = [get_next_position(starting_point, dir) for dir in initial_directions]
    pipe_a, pipe_b = pipe_map[x_a][y_a], pipe_map[x_b][y_b]
    direction_a = update_direction(initial_directions[0], pipe_a)
    direction_b = update_direction(initial_directions[1], pipe_b)
    while (x_a, y_a) != (x_b, y_b):
        (x_a, y_a)  = get_next_position((x_a, y_a), direction_a)
        (x_b, y_b) = get_next_position((x_b, y_b), direction_b)
        pipe_a, pipe_b = pipe_map[x_a][y_a], pipe_map[x_b][y_b]
        direction_a = update_direction(direction_a, pipe_a)
        direction_b = update_direction(direction_b, pipe_b)
        steps += 1
    return steps

if __name__ == '__main__':
    pipe_map = get_input("input.txt")
    starting_point = find_starting_point(pipe_map)
    initial_directions = find_initial_pipe_directions(starting_point, pipe_map)
    print(move_through_pipe(starting_point, initial_directions, pipe_map))
