"""Day 1: Trecuchet?!"""

from typing import Generator, List, Tuple
import argparse
import re


def identify_digit(data: str) -> List[Tuple[int, str]]:
    """
    Identify digit in a string

    Parameters
    ----------
    data : str
        Input data

    Returns
    -------
    List[Tuple[int, str]]
        List with index, digit
    """

    spelled_digit = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    # Identify digist
    digits = [(match.start(), match.group()) for match in re.finditer("\d", data)]

    # Identify spelling digist
    for spelling_digits in spelled_digit:
        matches = re.finditer(spelling_digits, data)
        if matches:
            digits += [(match.start(), spelled_digit[match.group()]) for match in matches]

    digits.sort(key=lambda x: x[0])

    return digits


def calibration_value_found(data: List[Tuple[int, str]]) -> int:
    """
    Return the combinig the first digit and the last digit

    Parameters
    ----------
    data : List[Tuple[int, str]]
        List with index, digit

    Returns
    -------
    int
        Single two-digit number
    """

    calibration_value = data[0][1] + data[-1][1]

    return int(calibration_value)


def data_reader(path: str) -> Generator:
    """
    _summary_

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
        for line in file.readlines():
            yield line


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Day 1: Trecuchet?!")
    parser.add_argument("--test", help="If is True, use test data", action="store_true")
    args = parser.parse_args()

    # Read data
    DATA_PATH = "day_01/test_data" if args.test else "day_01/data"

    digist_in_line = map(identify_digit, data_reader(DATA_PATH))
    sum_calibration_value = sum(map(calibration_value_found, digist_in_line))
    print(sum_calibration_value)
