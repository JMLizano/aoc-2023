from typing import List, Tuple


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
    
def find_almost_equal_lines(lines: List[str]) -> List[Tuple[int, int]]:
    almost_equals = []
    for i, line1 in enumerate(lines):
        for j, line2 in enumerate(lines[:i]):
            if sum(c1 != c2 for c1,c2 in zip(line1, line2)) == 1:
                almost_equals.append((i,j))
    return almost_equals



def find_consecutive_cut_points(cut_points: List[List[int]], reverse: bool = False):
    reference = cut_points[0]
    good_cuts = []
    for cut_point in reference:
        found = True
        end = cut_point + 1
        if cut_point == 0:
            good_cuts.append(cut_point)
            # return cut_point
        if reverse:
            end = len(cut_points) - cut_point
        for i in range(1, end):
            found = found & ( cut_point in cut_points[i] )
        if found:
            good_cuts.append(cut_point)
            # return cut_point
    return good_cuts


def find_mirror(lines: List[str]) -> int:
    possible_reflection_points = []
    for i, line in enumerate(lines):
        repeated = find_repeated_string(line, lines)
        cut_points = [get_cut_point(first=i, second=r) for r in repeated]
        cut_points = [c for c in cut_points if c is not None]
        possible_reflection_points.append(cut_points)
    # check for first and last
    cut_point = find_consecutive_cut_points(possible_reflection_points)
    # if not cut_point and cut_point != 0:
    cut_point += find_consecutive_cut_points(
        list(reversed(possible_reflection_points)),
        reverse=True
    )
    return cut_point


def transpose_string_list(string_list: List[str]):
    trasposed_lines = []
    for i in range(len(string_list[0])):
        new_line = ''.join([line[i] for line in string_list])
        trasposed_lines.append(new_line)
    return trasposed_lines


def find_horizontal_or_vertical_mirror(lines: List[str], do_vertical:bool = False):
    mirrors = find_mirror(lines)
    mirrors = [f"H{horizontal_mirror}" for horizontal_mirror in mirrors]
    # print("")
    # print("HORIZONTAL ", horizontal_mirror)
    # print("\n".join(lines))
    if do_vertical or not mirrors:
        transposed_lines = transpose_string_list(lines)
        vmirrors = find_mirror(transposed_lines)
        mirrors += [f"V{v}" for v in vmirrors]
        # print("")
        # print("VERTICAL ", vertical_mirror)
        # print("\n".join(lines))
    return mirrors


def find_mirror_after_fix(lines: List[str]):
    previous_mirror = find_horizontal_or_vertical_mirror(lines)[0]
    print("PREVIOS MIRROR ", previous_mirror)
    almost_equal_lines = find_almost_equal_lines(lines)
    for (i, j) in almost_equal_lines:
        modified_lines = lines[:]
        modified_lines[i] = modified_lines[j]
        new_mirrors = find_horizontal_or_vertical_mirror(modified_lines, do_vertical=True)
        for mirror in new_mirrors:
            if mirror != previous_mirror:
                return mirror
    transposed_lines = transpose_string_list(lines)
    almost_equal_lines = find_almost_equal_lines(transposed_lines)
    previous_mirror = previous_mirror.replace("H", "V") if previous_mirror.startswith("H") else previous_mirror.replace("V", "H")
    for (i, j) in almost_equal_lines:
        modified_lines = transposed_lines[:]
        modified_lines[i] = modified_lines[j]
        new_mirrors = find_horizontal_or_vertical_mirror(modified_lines, do_vertical=True)
        for mirror in new_mirrors:
            if mirror != previous_mirror:
                return mirror.replace("H", "V") if mirror.startswith("H") else mirror.replace("V", "H")
    print("MALA COSA WEY")
    print("\n".join(lines))


def get_value_from_cuts(values: List[str]):
    total = 0
    for value in values:
        print(value)
        if value.startswith("H"):
            total += (int(value.replace("H", "")) + 1) * 100
        else:
            total += (int(value.replace("V", "")) + 1)
    return total


if __name__ == '__main__':
    input = get_input("/Users/chema/personal/aoc-2023/day13/input.txt")
    fixed_cuts = [find_mirror_after_fix(lines) for lines in input]
    print(get_value_from_cuts(fixed_cuts))