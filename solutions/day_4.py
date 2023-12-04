from typing import List
import numpy as np


type Scratchcard = List[int, List[int], List[int]]


def get_scratchcards(data: str) -> List[Scratchcard]:
    scratchcards = []

    for row in data.split('\n'):
        card, numbers = row.split(':')
        card_id = int(card.split()[1])
        winning_numbers_str, card_numbers_str = numbers.strip().split('|')
        winning_numbers = [int(n) for n in winning_numbers_str.strip().split()]
        card_numbers = [int(n) for n in card_numbers_str.strip().split()]

        scratchcards.append([card_id, winning_numbers, card_numbers])

    return scratchcards


def get_winning_numbers(scratchcard: Scratchcard) -> List[int]:
    _, winning_numbers, card_numbers = scratchcard
    winning_card_numbers = list({n for n in card_numbers if n in winning_numbers})

    return winning_card_numbers


def calculate_card_points(scratchcard: Scratchcard) -> int:
    winning_numbers = get_winning_numbers(scratchcard)
    n_winning_numbers = len(winning_numbers)

    if n_winning_numbers == 0:
        card_points = 0
    else:
        card_points = 2**(n_winning_numbers - 1)

    return card_points


def count_scratchcards(scratchcards: List[Scratchcard]) -> List[int]:
    scratchcards_counts = [1 for _ in scratchcards]  # one copy of each card guaranteed

    for i, card in enumerate(scratchcards):
        winning_numbers = get_winning_numbers(card)
        n_winning_numbers = len(winning_numbers)

        for j in range(1, n_winning_numbers + 1):
            if i + j < len(scratchcards):
                scratchcards_counts[i + j] += scratchcards_counts[i]

    return scratchcards_counts


def get_part_1_answer(data: str) -> int:
    scratchcards = get_scratchcards(data)
    card_points = [calculate_card_points(card) for card in scratchcards]
    card_points_sum = sum(card_points)

    return card_points_sum


def get_part_2_answer(data: str) -> int:
    scratchcards = get_scratchcards(data)
    scratchcards_counts = count_scratchcards(scratchcards)
    scratchcards_count = sum(scratchcards_counts)

    print(scratchcards_counts)

    return scratchcards_count



