import argparse

from solutions.utils.print_answers import print_answers

from dotenv import load_dotenv
load_dotenv()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('day', type=int)
    parser.add_argument('-p', '--part', default=None, type=int)
    args = parser.parse_args()

    print_answers(day=args.day, year=2023, part=args.part)
