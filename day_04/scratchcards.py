"""Day 4: Scratchcards"""

from typing import Generator
import argparse
import re


def data_parser(data: str) -> int | None:
    """
    Parse data and return the power of 2.

    Parameters
    ----------
    data : str
        Data to parse.

    Returns
    -------
    int | None
        Power of 2 or None if no points.
    """
    match = re.search(r".*: (.+) \| (.+)", data)
    winning_numbers = set(match.group(1).split())
    having_numbers = set(match.group(2).split())
    points = having_numbers.intersection(winning_numbers)
    if points:
        return len(points)


def data_reader(path: str) -> Generator:
    """
    Read data from file

    Parameters
    ----------
    path : str
        Data path

    Yields
    ------
    Generator
        Line of data
    """
    with open(path, 'r') as file:
        for row, line in enumerate(file, 1):
            yield row, line


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Day 4: Scratchcards")
    parser.add_argument("--test", help="If is True, use test data", action="store_true")

    args = parser.parse_args()
    DATA_PATH = "day_04/test_data" if args.test else "day_04/data"

    with open(DATA_PATH, 'r') as file:
        cards = len(file.readlines())
    scratchcards = {row + 1: 0 for row in range(cards)}

    for row, line in data_reader(DATA_PATH):
        scratchcards[row] += 1
        winnig_cards = data_parser(line)
        if winnig_cards:
            for row_winning in range(row + 1, row + winnig_cards + 1):
                if row_winning in scratchcards:
                    scratchcards[row_winning] += scratchcards[row]

    print(sum(scratchcards.values()))
