"""Day 3: Gear Ratios"""

from operator import mul
from typing import Dict, Generator, List, Tuple
import argparse
import linecache
import re

DATA_PATH: str = ""


def extract_elements(data: str, line_number: int, regex: str) -> List[Tuple[int | str]]:
    """
    Extract a list with string and their coordinates from a string

    Parameters
    ----------
    data : str
        Input data.
    line_number : int
        Line number.
    regex : str
        Regex to extract elements.

    Returns
    -------
    List[Tuple[int | str]]
        List with elements and their coordinates.
    """
    regex_digist = list(re.finditer(regex, data))
    if regex_digist:
        return [(match.group(), line_number, match.start(), match.end()) for match in regex_digist]
    else:
        return []


def add_numbers_in_gears(gears: Dict[Tuple[int | str], List]) -> Dict[Tuple[int | str], List]:
    """
    Add numbers in gears dictionary.

    Parameters
    ----------
    gears : Dict[Tuple[int  |  str], List]
        Gears dictionary.

    Returns
    -------
    Dict[Tuple[int | str], List]
        Gears dictionary with numbers.
    """

    # Read lines
    for gear in gears:
        columns_gear = set(range(gear[2] - 1, gear[3] + 1))
        for lines in range(gear[1] - 1, gear[1] + 2):
            data = linecache.getline(DATA_PATH, lines).strip()
            numbers = extract_elements(data, lines, r"\d+")
            for number in numbers:
                columns_numer = set(range(number[2], number[3]))
                if columns_gear.intersection(columns_numer):
                    gears[gear].append(number)

    return gears


def extract_gears(numbers: List[Tuple[str | int]]) -> int:
    """
    Extract gears from numbers

    Parameters
    ----------
    numbers : List[Tuple[str  |  int]]
        Numbers in gear.

    Returns
    -------
    int
        Number of gears.
    """
    if len(numbers) == 2:
        return mul(*map(lambda x: int(x[0]), numbers))
    else:
        return 0


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
        for line_number, line in enumerate(file, start=1):
            yield line_number, line


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Day 3: Gear Ratios")
    parser.add_argument("--test", help="If is True, use test data", action="store_true")

    args = parser.parse_args()
    DATA_PATH = "day_03/test_data" if args.test else "day_03/data"

    CUMULATIVE_SUM = 0
    GEARS = dict()
    for l_number, line_row in data_reader(DATA_PATH):
        gears_coordinates = extract_elements(line_row, l_number, r"\*")
        tmp_gears = {gear: [] for gear in gears_coordinates}
        GEARS.update(tmp_gears)

    GEARS = add_numbers_in_gears(GEARS)

    print(sum(map(extract_gears, GEARS.values())))
