
import itertools
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


def navigate(instructions: str, nodes: Dict[str, Tuple[str, str]]):
    steps = 0
    current = "AAA"
    for character in itertools.cycle(instructions):
        steps += 1
        childs = nodes[current]
        if character == "L":
            current = childs[0]
        else:
            current = childs[1]
        if current == "ZZZ":
            return steps


if __name__ == '__main__':
    input = get_input("input.txt")
    instructions, nodes = get_instructions_and_nodes(input)
    print(navigate(instructions, nodes))
