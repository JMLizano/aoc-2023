
import itertools
import math
import multiprocessing
from functools import partial, reduce
from typing import Dict, List, Tuple


def get_input(filepath: str):
    with open(filepath, "r") as f:
        return f.read().splitlines()


def get_instructions_and_nodes(input: List[str]):
    instructions = input[0]
    nodes = {}
    for line in input[2:]:
        root, child = line.split(" = ")
        child_left, child_right = child.strip("()").split(", ")
        nodes[root] = (child_left, child_right)
    return instructions, nodes


def navigate(instructions: str, nodes: Dict[str, Tuple[str, str]], current: str):
    steps = 0
    for character in itertools.cycle(instructions):
        steps += 1
        childs = nodes[current]
        if character == "L":
            current = childs[0]
        else:
            current = childs[1]
        if current.endswith("Z"):
            return steps


def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)


def navigate_all(instructions: str, nodes: Dict[str, Tuple[str, str]]):
    starting_nodes = [node for node in nodes.keys() if node.endswith("A")]
    partial_navigate = partial(navigate, instructions, nodes)
    with multiprocessing.Pool(8) as pool:
        results = pool.map(partial_navigate, starting_nodes)
    return reduce(lcm, results)


if __name__ == '__main__':
    input = get_input("input.txt")
    instructions, nodes = get_instructions_and_nodes(input)
    print(navigate_all(instructions, nodes))
