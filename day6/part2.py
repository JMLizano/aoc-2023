import math
from typing import List, Tuple


def get_input(filepath: str):
    with open(filepath, "r") as f:
        return f.read().splitlines()

def get_times_and_distance(input: List[str]) -> Tuple[int, int]:
    times = input[0].replace("Time:","").strip().replace(" ", "")
    distances = input[1].replace("Distance:","").strip().replace(" ", "")
    times = int(times)
    distances = int(distances)
    return times, distances

def get_solutions(time, distance) -> List[int]:
    root_1 = time / 2 - 0.5 * math.sqrt(time * time - 4 * distance)
    root_2 = time / 2 + 0.5 * math.sqrt(time * time - 4 * distance)
    root_1 = math.ceil(root_1) if root_1 != math.ceil(root_1) else math.ceil(root_1) + 1
    root_2 = math.ceil(root_2) if root_1 != math.ceil(root_2) else math.ceil(root_2) - 1
    return root_2 - root_1

if __name__ == '__main__':
    input = get_input("input.txt")
    time, distance = get_times_and_distance(input)
    print(get_solutions(time, distance))
    