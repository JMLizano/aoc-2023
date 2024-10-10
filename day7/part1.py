from collections import defaultdict
from typing import List, Tuple
from functools import cmp_to_key


def get_input(filepath: str):
    with open(filepath, "r") as f:
        lines = f.read().splitlines()
        lines = [(line.split()[0],line.split()[1]) for line in lines]
        return [
            (hand, int(bid))
            for (hand, bid) in lines
        ]

def get_hand_type(hand: str) -> Tuple[str, int]:
    counts = defaultdict(lambda: 0)
    for card in hand:
        counts[card] += 1
    c = set(counts.values())
    if c == {5}:
        return 7
    if c == {4, 1}:
        return 6
    if c == {3, 2}:
        return 5
    if c == {3, 1}:
        return 4
    if c == {2, 1} and len(counts.values()) == 3:
        return 3
    if c == {2, 1} and len(counts.values()) == 4:
        return 2
    if c == {1}:
        return 1

def get_high_card(hand1, hand2):
    values_map = {"A": 5, "K": 4, "Q": 3, "J": 2, "T": 1}
    for card1, card2 in zip(hand1, hand2):
        if card1.isnumeric() and card2.isnumeric():
            if card1 > card2:
                return 1
            elif card2 > card1:
                return -1
        elif card1.isnumeric() and not card2.isnumeric():
            return -1
        elif not card1.isnumeric() and card2.isnumeric():
            return 1
        else:
            if values_map[card1] > values_map[card2]:
                return 1
            elif values_map[card2] > values_map[card1]:
                return -1
    return 0


def compare_hands(hand_type1, hand_type2):
    hand1, type1, _ = hand_type1
    hand2, type2, _ = hand_type2
    if type1 > type2:
        return 1
    if type2 > type1:
        return -1
    return get_high_card(hand1, hand2)


def sort_hands(hands: List[Tuple[str, int]]):
    hands = [
        (hand, get_hand_type(hand), bid)
        for (hand, bid) in hands
    ]
    return sorted(hands, key=cmp_to_key(compare_hands))


if __name__ == '__main__':
    input = get_input("/Users/chema/personal/aoc-2023/day7/input.txt")
    sorted_hands = sort_hands(input)
    total_bid = 0
    for ranking, hand in enumerate(sorted_hands, 1):
        total_bid += ranking * hand[2]
    print(total_bid)