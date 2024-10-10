from itertools import permutations, combinations

def get_input(filepath: str):
    with open(filepath, "r") as f:
        return f.read().splitlines()


def get_galaxies_and_expandable(input):
    galaxies = set()
    for x, line in enumerate(input):
        for y,char in enumerate(line): 
            if char == "#":
                galaxies.add((x,y))
    expandable_rows = set([r for r in range(len(input)) if r not in [x for x,y in galaxies]])
    expandable_columns = set([c for c in range(len(input[0])) if c not in [y for x,y in galaxies]])
    return galaxies, expandable_columns, expandable_rows

def manhattan_distance(pos_a, pos_b):
    return abs(pos_b[1] - pos_a[1]) + abs(pos_b[0] - pos_a[0])


def increment_distance(pos_a, pos_b, expandable_columns, expandable_rows):
    min_row = pos_a[0] if pos_a[0] <= pos_b[0] else pos_b[0]
    max_row = pos_a[0] if pos_a[0] > pos_b[0] else pos_b[0]
    min_col = pos_a[1] if pos_a[1] <= pos_b[1] else pos_b[1]
    max_col = pos_a[1] if pos_a[1] > pos_b[1] else pos_b[1]
    distance = 0
    for row in expandable_rows:
        if min_row < row < max_row:
            distance += 999999
    for col in expandable_columns:
        if min_col < col < max_col:
            distance += 999999
    return distance


def get_distances(galaxies, expandable_columns, expandable_rows):
    total_distance = 0
    print(expandable_columns)
    print(expandable_rows)
    for pos_a, pos_b in combinations(galaxies, 2):
        initial_distance = manhattan_distance(pos_a, pos_b)
        print(pos_a,pos_b, initial_distance)
        initial_distance += increment_distance(pos_a, pos_b, expandable_columns, expandable_rows)
        print(pos_a,pos_b, initial_distance)
        total_distance += initial_distance
    return total_distance


if __name__ == '__main__':
    input = get_input("input.txt")
    gal,expc,expr = get_galaxies_and_expandable(input)
    print(get_distances(gal, expc, expr))