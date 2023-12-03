from typing import List
import numpy as np
import re


def get_engine_schematic(data: str) -> np.ndarray:
    engine_schematic = np.array([np.array(list(row)) for row in data.split('\n')])

    return engine_schematic


def get_direct_symbol_adjacency_mask(engine_schematic: np.ndarray, symbols_pattern: str) -> np.ndarray:
    is_directly_adjacent_to_symbol = np.full(np.shape(engine_schematic), False)

    n_rows = np.shape(engine_schematic)[0]
    n_cols = np.shape(engine_schematic)[1]

    for i in range(n_rows):
        for j in range(n_cols):
            if re.search(symbols_pattern, str(engine_schematic[i, j])):
                is_directly_adjacent_to_symbol[i-1:i+2, j-1:j+2] = True
                is_directly_adjacent_to_symbol[i, j] = False

    return is_directly_adjacent_to_symbol


def get_part_number_mask(engine_schematic: np.ndarray, symbols_pattern: str) -> np.ndarray:
    is_directly_adjacent_to_symbol = get_direct_symbol_adjacency_mask(engine_schematic, symbols_pattern)
    is_part_number = is_directly_adjacent_to_symbol.copy()

    n_rows = np.shape(engine_schematic)[0]
    n_cols = np.shape(engine_schematic)[1]

    # checking from left to right
    for i in range(n_rows):
        for j in range(n_cols - 1):
            # current item is a part number and next item is a digit, mark that as part number as well
            if engine_schematic[i, j] in list('0123456789') and is_part_number[i, j] and engine_schematic[i, j + 1] in list('0123456789'):
                is_part_number[i, j + 1] = True

    # checking from right to left
    for i in range(n_rows - 1, -1, -1):
        for j in range(n_cols - 1, 0, -1):
            # current item is a part number and previous item is a digit, mark that as part number as well
            if engine_schematic[i, j] in list('0123456789') and is_part_number[i, j] and engine_schematic[i, j - 1] in list('0123456789'):
                is_part_number[i, j - 1] = True

    for i in range(n_rows):
        for j in range(n_cols):
            if engine_schematic[i, j] == '.':
                is_part_number[i, j] = False

    return is_part_number


def get_part_numbers(engine_schematic: np.ndarray, symbols_pattern: str) -> List[int]:
    is_part_number = get_part_number_mask(engine_schematic, symbols_pattern)
    part_numbers = []

    n_rows = np.shape(engine_schematic)[0]
    n_cols = np.shape(engine_schematic)[1]

    current_number_str = ''
    for i in range(n_rows):
        for j in range(n_cols):
            if is_part_number[i, j]:
                current_number_str += engine_schematic[i, j]
            else:
                if len(current_number_str) > 0:
                    current_number = int(current_number_str)
                    part_numbers.append(current_number)

                    current_number_str = ''

        if len(current_number_str) > 0:
            current_number = int(current_number_str)
            part_numbers.append(current_number)

            current_number_str = ''

    return part_numbers


def get_gear_ratios(engine_schematic: np.ndarray) -> List[int]:
    gear_ratios = []

    n_rows = np.shape(engine_schematic)[0]
    n_cols = np.shape(engine_schematic)[1]
    max_part_number_length = len(str(max(get_part_numbers(engine_schematic, '[^0-9.]'))))

    for i in range(n_rows):
        for j in range(n_cols):
            if engine_schematic[i, j] == '*':
                star_adjacent_schema = engine_schematic[i-1:i+2, j-max_part_number_length:j+max_part_number_length+1].copy()

                # remove other symbols in the vicinity
                star_adjacent_schema[~np.isin(star_adjacent_schema, list('0123456789'))] = '.'

                # restore the current star (in the center now)
                star_adjacent_schema[1, max_part_number_length] = '*'

                # get part numbers for that star
                star_adjacent_part_numbers = get_part_numbers(star_adjacent_schema, '[*]')

                if len(star_adjacent_part_numbers) == 2:
                    gear_ratio = star_adjacent_part_numbers[0] * star_adjacent_part_numbers[1]
                    gear_ratios.append(gear_ratio)

    return gear_ratios


def get_part_1_answer(data: str) -> int:
    engine_schematic = get_engine_schematic(data)
    part_numbers = get_part_numbers(engine_schematic, symbols_pattern='[^0-9.]')
    part_numbers_sum = sum(part_numbers)

    return part_numbers_sum


def get_part_2_answer(data: str) -> int:
    engine_schematic = get_engine_schematic(data)
    gear_ratios = get_gear_ratios(engine_schematic)
    gear_ratios_sum = sum(gear_ratios)

    return gear_ratios_sum
