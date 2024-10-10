from typing import Dict, List, Tuple

def get_input(filepath: str):
    with open(filepath, "r") as f:
        return f.readlines()


def process_game(game_line: str) -> Tuple[int, List[Dict[str, int]]]:
    game_id, sets = game_line.split(":")
    game_id = int(game_id.split(" ")[1])
    set_list = sets.split(";")
    gamesets = []
    for gameset in set_list:
        cubes = gameset.split(",")
        cubecount = {}
        for cube in cubes:
            numcubes, color = cube.strip().split(" ")
            cubecount[color] = int(numcubes)
        gamesets.append(cubecount)

    return game_id, gamesets

def validate_game(game: List[Dict[str, int]], maximum_values: Dict[str, int]):
    for gameset in game:
        for color, numcubes in gameset.items():
            if numcubes > maximum_values[color]:
                return False
    return True

def get_valid_games(game_lines: List[str], maximum_values = {"red": 12, "blue": 14, "green": 13}) -> int:
    sumgamesid = 0
    for game in game_lines:
        game_id, gamesets = process_game(game.replace("\n", ""))
        if validate_game(gamesets, maximum_values):
            sumgamesid += game_id
    return sumgamesid

if __name__ == '__main__':
    game_lines = get_input("input.txt")
    print(get_valid_games(game_lines))