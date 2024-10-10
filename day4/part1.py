from typing import Set, Tuple



def get_input(filepath: str):
    with open(filepath, "r") as f:
        return f.read().splitlines()


def process_line(line: str) -> Tuple[Set[int], Set[int]]:
    card, number_sets = line.split(":")
    winning_numbers, my_numbers = number_sets.split("|")
    winning_numbers = winning_numbers.strip().split(" ")
    winning_numbers = {int(number) for number in winning_numbers if number != ''}
    my_numbers = my_numbers.strip().split(" ")
    my_numbers = {int(number) for number in my_numbers if number != ''}
    return winning_numbers, my_numbers

def get_card_value(winning_numbers: Set[int], my_numbers: Set[int]) -> int:
    winning_numbers_count = len(winning_numbers.intersection(my_numbers))
    if winning_numbers_count > 0:
        return 2 ** (winning_numbers_count - 1)
    return 0

if __name__ == '__main__':
    input = get_input("input.txt")
    cards = [process_line(line) for line in input]
    cards_value = [get_card_value(winning_numbers,my_numbers) for winning_numbers,my_numbers in cards]
    print(sum(cards_value))
