from typing import Optional
from importlib import import_module
from aocd import get_data

from solutions.utils.timing import timeit


def print_answers(day: int, year: int, part: Optional[int]) -> None:
    def print_part_answers(data: str, module: str, part: int) -> None:
        part_fun = getattr(module, f'get_part_{part}_answer', None)
        if part_fun:
            answer, time = timeit(part_fun)(data)
            print(f'Part {part} answer: {answer}\n'
                  f'⏱️  {time:.3f} ms\n')
        else:
            print(f'Part {part} is not solved yet... ⏳️')

    print(f'-- 📅 {year} day {day} --')

    data = get_data(day=day, year=year)
    module = import_module(f'solutions.day_{day}')

    if part is not None:
        print_part_answers(data, module, part)

    else:
        print_part_answers(data, module, 1)
        print_part_answers(data, module, 2)
