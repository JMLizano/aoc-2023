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


def get_winning_numbers(winning_numbers: Set[int], my_numbers: Set[int]) -> int:
    return len(winning_numbers.intersection(my_numbers))


def get_total_cards(cards) -> int:
    cards_count = {i: 1 for i in range(1, len(cards) + 1)}
    for card_number, (winning_numbers, my_numbers) in enumerate(cards, 1):
        winning_numbers = get_winning_numbers(winning_numbers, my_numbers)
        for i in range(card_number + 1, card_number + winning_numbers + 1):
            cards_count[i] += cards_count[card_number]
    return sum(cards_count.values())


if __name__ == '__main__':
    input = get_input("input.txt")
    cards = [process_line(line) for line in input]
    print(get_total_cards(cards))
