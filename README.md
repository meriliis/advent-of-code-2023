# Advent of Code 2023

Puzzles can be found on https://adventofcode.com/2023.

## Setup

### Virtual Environment

Poetry environment is used in this project. To install all the necessary libraries, run

`poetry install` 

anywhere in the project.

### Advent of Code session ID

Instead of copy-pasting input data from Advent of Code page, I read my personal input data using [`advent-of-code-data` library](https://github.com/wimglenn/advent-of-code-data). 

To test the solutions on your own data, create a `.env` file similar to `.env.example` and add there your Advent of Code session cookie, which you can find using your browser inspector. 

### Running

To get solutions for any day, run 

``poetry run python main.py <day number>``

from the project root folder. You can optionally specify part one or two with `-p`, e.g. `poetry run python main.py 1 -p 1`