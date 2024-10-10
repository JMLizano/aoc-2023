from typing import Dict, List
from functools import reduce


def get_input(filepath: str):
    with open(filepath, "r") as f:
        return f.readlines()


def process_game(game_line: str) -> List[Dict[str, int]]:
    game = game_line.split(":")[1]
    set_list = game.split(";")
    gamesets = []
    for gameset in set_list:
        cubes = gameset.split(",")
        cubecount = {}
        for cube in cubes:
            numcubes, color = cube.strip().split(" ")
            cubecount[color] = int(numcubes)
        gamesets.append(cubecount)

    return gamesets


def get_maximum_cubes_by_color(game: List[Dict[str, int]]):
    minimum_required = {"red": 0, "blue": 0, "green": 0}
    for gameset in game:
        for color, numcubes in gameset.items():
            minimum_required[color] = max(minimum_required[color], numcubes)
    return minimum_required


def get_game_powers(game_lines: List[str]) -> int:
    sumgamespower = 0
    for game in game_lines:
        gamesets = process_game(game.replace("\n", ""))
        minimum_required_cubes = get_maximum_cubes_by_color(gamesets)
        sumgamespower += reduce(lambda a,b: a * b, minimum_required_cubes.values())
    return sumgamespower


if __name__ == '__main__':
    game_lines = get_input("input.txt")
    print(get_game_powers(game_lines))