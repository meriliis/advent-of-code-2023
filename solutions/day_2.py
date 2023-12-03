from typing import List
from functools import reduce


type Game = List[dict[str, int]]

def get_games_data(data:str) -> dict[int, Game]:
    rows = data.split('\n')
    games = dict()

    for row in rows:
        game_name, results_str = row.split(': ')
        game_id = int(game_name.split(' ')[1])

        games[game_id] = [
            {
                color: int(n)
                for n, color in [tuple(n_color.split(' ')) for n_color in result_str.split(', ')]
            }
            for result_str in results_str.split('; ')
        ]

    return games


def is_possible(game: Game, setup: dict[str, int]) -> bool:
    for result in game:
        for color, n in result.items():
            if n > setup[color]:
                return False

    return True


def get_min_setup(game: Game) -> dict[str, int]:
    min_results = {
        'red': 0
        , 'green': 0
        , 'blue': 0
    }

    for result in game:
        for color, n in result.items():
            if n > min_results[color]:
                min_results[color] = n

    return min_results


def get_setup_power(setup: dict[str, int]) -> int:
    setup_power = reduce(lambda x, y: x * y, setup.values())

    return setup_power


def get_part_1_answer(data: str) -> int:
    setup = {
        'red': 12
        , 'green': 13
        , 'blue': 14
    }

    games = get_games_data(data)
    possible_game_ids = [game_id for game_id, game in games.items() if is_possible(game, setup)]
    possible_game_ids_sum = sum(possible_game_ids)

    return possible_game_ids_sum


def get_part_2_answer(data: str) -> int:
    games = get_games_data(data)
    min_setups = [get_min_setup(game) for game in games.values()]
    print(min_setups)

    min_setup_powers = [get_setup_power(setup) for setup in min_setups]
    min_setup_powers_sum = sum(min_setup_powers)

    return min_setup_powers_sum