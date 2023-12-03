from typing import List
import re


STRING_TO_DIGIT_MAP = {
    'one': '1'
    , 'two': '2'
    , 'three': '3'
    , 'four': '4'
    , 'five': '5'
    , 'six': '6'
    , 'seven': '7'
    , 'eight': '8'
    , 'nine': '9'
}


def get_calibration_document_rows(data: str) -> List[str]:
    return data.split('\n')


def keep_digits(row: str) -> str:
    return re.sub('[^1-9]', '', row)


def replace_first_string_with_digit(row: str) -> str:
    matches = list(re.finditer('(?=(' + '|'.join(STRING_TO_DIGIT_MAP.keys()) + '))', row))

    if matches:
        first_match = matches[0].group(1)
        row = re.sub(first_match, STRING_TO_DIGIT_MAP[first_match], row)

    return row


def replace_last_string_with_digit(row: str) -> str:
    matches = list(re.finditer('(?=(' + '|'.join(STRING_TO_DIGIT_MAP.keys()) + '))', row))

    if matches:
        last_match = matches[-1].group(1)
        row = re.sub(last_match, STRING_TO_DIGIT_MAP[last_match], row)

    return row


def get_part_1_answer(data: str) -> int:
    calibration_document_rows = get_calibration_document_rows(data)
    calibration_document_rows_digits = [keep_digits(row) for row in calibration_document_rows]
    calibration_values = [int(row[0] + row[-1]) for row in calibration_document_rows_digits]
    calibration_values_sum = sum(calibration_values)

    return calibration_values_sum


def get_part_2_answer(data: str) -> int:
    calibration_document_rows = get_calibration_document_rows(data)
    calibration_document_rows_with_replaced_digits = [
        (replace_first_string_with_digit(row), replace_last_string_with_digit(row))
        for row in calibration_document_rows
    ]

    calibration_document_rows_digits = [
        (keep_digits(row1), keep_digits(row2))
        for row1, row2 in calibration_document_rows_with_replaced_digits
    ]

    calibration_values = [int(row1[0] + row2[-1]) for row1, row2 in calibration_document_rows_digits]
    calibration_values_sum = sum(calibration_values)

    return calibration_values_sum