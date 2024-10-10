import math
from typing import List, Tuple


def get_input(filepath: str):
    with open(filepath, "r") as f:
        return f.read().splitlines()

def get_times_and_distance(input: List[str]) -> List[Tuple[int, int]]:
    times = input[0].replace("Time:","").strip().split()
    distances = input[1].replace("Distance:","").strip().split()
    times = [int(t) for t in times]
    distances = [int(d) for d in distances]
    return zip(times, distances)

def get_solutions(time, distance) -> List[int]:
    root_1 = time / 2 - 0.5 * math.sqrt(time ** 2 - 4 * distance)
    root_2 = time / 2 + 0.5 * math.sqrt(time ** 2 - 4 * distance)
    solutions = list(range(math.ceil(root_1), math.ceil(root_2 )))
    return [sol for sol in solutions if sol != root_1 and sol != root_2]

if __name__ == '__main__':
    input = get_input("input.txt")
    possible_solutions = 1
    for time, distance in get_times_and_distance(input):
        print(get_solutions(time, distance))
        possible_solutions *= len(get_solutions(time, distance))
    print(possible_solutions)
    