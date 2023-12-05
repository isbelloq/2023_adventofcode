"""Day 3: Gear Ratios"""
import argparse
from typing import List, Tuple, Generator
import linecache
import re

DATA_PATH: str = ""
TOTAL_LINES: int = 0
MAX_RIGHT: int = 0


def extract_numbers(data: str, line_number: int) -> List[Tuple[int]] | None:
    """
    Extract a list with numbers and their coordinates from a string

    Parameters
    ----------
    data : str
        Input data
    line_number : int
        Line number

    Returns
    -------
    List[Tuple[int]] | None
        List with numbers and their coordinates
    """
    regex_digist = list(re.finditer(r"\d+", data))
    if regex_digist:
        return [(int(match.group()), line_number, match.start(), match.end()) for match in regex_digist]


def validate_number(number: Tuple[int]) -> int:
    """
    Validate if number is valid based on surrounding characters

    Parameters
    ----------
    number : Tuple[int]
        Number and its coordinates

    Returns
    -------
    int
        Valid number or 0 if not valid
    """
    upper_read_line = number[1] - 1
    lower_read_line = number[1] + 1

    left_read_line = number[2] if number[2] == 0 else number[2] - 1
    right_read_line = number[3] if number[3] == MAX_RIGHT else number[3] + 1

    # Read lines

    upper_line = "" if upper_read_line <= 1 else linecache.getline(DATA_PATH, upper_read_line).strip()
    mid_line = linecache.getline(DATA_PATH, number[1]).strip()
    lower_line = "" if lower_read_line >= TOTAL_LINES else linecache.getline(DATA_PATH, lower_read_line).strip()

    validation_string = upper_line[left_read_line: right_read_line]\
        + mid_line[left_read_line: right_read_line]\
        + lower_line[left_read_line: right_read_line]

    if re.search(r"[^\d\.]", validation_string):
        return number[0]
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

    with open(DATA_PATH, 'r') as file:
        TOTAL_LINES = len(file.readlines())

    with open(DATA_PATH, 'r') as file:
        MAX_RIGHT = len(file.readlines()[0].strip())

    cumulative_sum = 0
    for l_number, line in data_reader(DATA_PATH):
        numbers_coordinates = extract_numbers(line, l_number)
        if numbers_coordinates:
            for number_coordinates in numbers_coordinates:
                cumulative_sum += validate_number(number_coordinates)

    print(cumulative_sum)
