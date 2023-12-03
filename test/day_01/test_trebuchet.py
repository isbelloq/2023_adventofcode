"""Unint test for Day 1: Trecuchet?!"""

from typing import List, Tuple

import pytest

from day_01.trebuchet import calibration_value_found, identify_digit


@pytest.mark.parametrize(
    "data, expected_digist",
    [
        ["two1nine", [(0, "2"), (3, "1"), (4, "9")]],
        ["eightwothree", [(0, "8"), (4, "2"), (7, "3")]],
        ["abcone2threexyz", [(3, "1"), (6, "2"), (7, "3")]],
        ["xtwone3four", [(1, "2"), (3, "1"), (6, "3"), (7, "4")]],
        ["4nineeightseven2", [(0, "4"), (1, "9"), (5, "8"), (10, "7"), (15, "2")]],
        ["zoneight234", [(1, "1"), (3, "8"), (8, "2"), (9, "3"), (10, "4")]],
        ["7pqrstsixteen", [(0, "7"), (6, "6")]],
    ]
)
def test_identify_digit(data: str, expected_digist: List[Tuple[int, str]]) -> None:
    """
    Test identify_digit function

    Parameters
    ----------
    data : str
        Input data
    expected_digist : List[Tuple[int, str]]
        List with index, digit
    """

    digist = identify_digit(data)

    assert isinstance(digist, list)
    assert digist == expected_digist


@pytest.mark.parametrize(
    "data, expected_calibration_value",
    [
        [[(0, "2"), (3, "1"), (4, "9")], 29],
        [[(0, "8"), (4, "2"), (7, "3")], 83],
        [[(3, "1"), (6, "2"), (7, "3")], 13],
        [[(1, "2"), (3, "1"), (6, "3"), (7, "4")], 24],
        [[(0, "4"), (1, "9"), (5, "8"), (10, "7"), (15, "2")], 42],
        [[(1, "1"), (3, "8"), (8, "2"), (9, "3"), (10, "4")], 14],
        [[(0, "7"), (6, "6")], 76],
        [[(0, "1"), (4, "2")], 12],
        [[(3, "3"), (7, "8")], 38],
        [[(1, "1"), (3, "2"), (5, "3"), (7, "4"), (9, "5")], 15],
        [[(4, "7")], 77]
    ]
)
def test_calibration_value_found(data: List[Tuple[int, str]], expected_calibration_value: int) -> None:
    """
    Test calibration_value_found function

    Parameters
    ----------
    data : List[Tuple[int, str]]
        List with index, digit
    calibration_value : int
        Single two-digit number
    """

    calibration_value = calibration_value_found(data)

    assert isinstance(calibration_value, int)
    assert (calibration_value > 10) & (calibration_value <= 99)
    assert calibration_value == expected_calibration_value
