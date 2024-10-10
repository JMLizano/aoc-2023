from typing import List


def get_input(filepath: str):
    with open(filepath, "r") as f:
        return [l.split("\n") for l in f.read().split("\n\n")]


def find_repeated_string(to_find: str, string_list: List[str]):
    indices = []
    for i, line in enumerate(string_list):
        if line == to_find:
            indices.append(i)
    return indices


def get_cut_point(first: int, second: int) -> int:
    distance = second - first - 1
    if distance % 2 != 0 or first == second:
        return None
    else:
        return first + distance // 2
    

def find_consecutive_cut_points(cut_points: List[List[int]], reverse: bool = False):
    reference = cut_points[0]
    for cut_point in reference:
        found = True
        end = cut_point + 1
        if cut_point == 0:
            return cut_point
        if reverse:
            end = len(cut_points) - cut_point
        for i in range(1, end):
            found = found & ( cut_point in cut_points[i] )
        if found:
            return cut_point

def find_mirror(lines: List[str]) -> int:
    possible_reflection_points = []
    for i, line in enumerate(lines):
        repeated = find_repeated_string(line, lines)
        cut_points = [get_cut_point(first=i, second=r) for r in repeated]
        cut_points = [c for c in cut_points if c is not None]
        possible_reflection_points.append(cut_points)
    # check for first and last
    cut_point = find_consecutive_cut_points(possible_reflection_points)
    if not cut_point and cut_point != 0:
        cut_point = find_consecutive_cut_points(
            list(reversed(possible_reflection_points)),
            reverse=True
        )
    return cut_point

def find_horizontal_or_vertical_mirror(lines: List[str]):
    horizontal_mirror = find_mirror(lines)
    print("")
    print("HORIZONTAL ", horizontal_mirror)
    print("\n".join(lines))
    if not horizontal_mirror and horizontal_mirror !=0:
        trasposed_lines = []
        for i in range(len(lines[0])):
            new_line = ''.join([line[i] for line in lines])
            trasposed_lines.append(new_line)
        vertical_mirror = find_mirror(trasposed_lines)
        print("")
        print("VERTICAL ", vertical_mirror)
        print("\n".join(lines))
        return vertical_mirror + 1
    return 100 * (horizontal_mirror + 1)

if __name__ == '__main__':
    input = get_input("/Users/chema/personal/aoc-2023/day13/input.txt")
    print(sum(find_horizontal_or_vertical_mirror(i) for i in input))