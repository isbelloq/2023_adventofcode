"""Unint test for Day 3: Gear Ratios"""

from typing import List, Tuple
from unittest import mock
import linecache

import pytest

from day_03.gear_ratios import extract_numbers, validate_number


@pytest.mark.parametrize(
    "data, line, expected_coordinate",
    [
        ["467..114..", 1, [(467, 1, 0, 3), (114, 1, 5, 8)]],
        ["...*......", 2, None],
        [".....+.58.", 6, [(58, 6, 7, 9)]],
        ["...$.*....", 9, None]
    ]
)
def test_extract_numbers(data: str, line: int, expected_coordinate: List[Tuple[int]] | None) -> None:
    """
    Test extract_numbers function

    Parameters
    ----------
    data : str
        Input data
    line : int
        Line number
    expected_coordinate : List[Tuple[int]] | None
        List with expected number coordinate
    """
    coordinate = extract_numbers(data, line)
    assert coordinate == expected_coordinate
    if coordinate:
        assert isinstance(coordinate, list)
        for element in coordinate:
            assert isinstance(element, tuple)
            assert len(element) == 4


@pytest.mark.parametrize(
    "number, mock_lines, expected_number",
    [
        [(35, 3, 2, 4), ["...*......", "..35..633.", "......#..."], 35],
        [(114, 1, 5, 8), ["no upper", "467..114..", "...*......"], 0],
        [(467, 1, 0, 3), ["no upper", "467..114..", "...*......"], 467],
    ]
)
def test_validate_number(number: Tuple[int], mock_lines: List[str], expected_number: int) -> None:
    """
    Test validate_number function

    Parameters
    ----------
    number : Tuple[int]
        Number and its coordinates
    mock_lines : List[str]
        Mock upper, mid and lower lines
    expected_number : int
        Expected valid number
    """
    with mock.patch(
        "day_03.gear_ratios.DATA_PATH", new="day_03/test_data"
        ), mock.patch(
        "day_03.gear_ratios.TOTAL_LINES", new=10
        ), mock.patch(
        "day_03.gear_ratios.MAX_RIGHT", new=11
        ), mock.patch.object(
            linecache, "getline"
            ) as mock_getline:
        mock_responses = {
            ("day_03/test_data", number[1] - 1): mock_lines[0],
            ("day_03/test_data", number[1]): mock_lines[1],
            ("day_03/test_data", number[1] + 1): mock_lines[2]
        }
        mock_getline.side_effect = lambda filename, lineno: mock_responses.get((filename, lineno))
        number = validate_number(number)

        assert number == expected_number
