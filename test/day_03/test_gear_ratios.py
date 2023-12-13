"""Unint test for Day 3: Gear Ratios"""

from typing import Dict, List, Tuple
from unittest import mock
import linecache

import pytest

from day_03.gear_ratios import add_numbers_in_gears, extract_elements, extract_gears


@pytest.mark.parametrize(
    "data, line, regex, expected_coordinate",
    [
        ["467..114..", 1, r"\d+", [("467", 1, 0, 3), ("114", 1, 5, 8)]],
        ["...*......", 2, r"\d+", []],
        ["...*......", 2, r"\*", [("*", 2, 3, 4)]],
        [".....+.58.", 6, r"\d+", [("58", 6, 7, 9)]],
        ["...$.*....", 9, r"\d+", []]
    ]
)
def test_extract_elements(data: str, line: int, regex: str, expected_coordinate: List[Tuple[int]]) -> None:
    """
    Test extract_elements function

    Parameters
    ----------
    data : str
        Line of data.
    line : int
        Line number.
    regex : str
        Regex to extract elements.
    expected_coordinate : List[Tuple[int]]
        Expected list with elements and their coordinates.
    """
    coordinate = extract_elements(data, line, regex)
    assert coordinate == expected_coordinate
    if coordinate:
        assert isinstance(coordinate, list)
        for element in coordinate:
            assert isinstance(element, tuple)
            assert len(element) == 4


@pytest.mark.parametrize(
    "gear, mock_lines, expected_dict",
    [
        [{("*", 2, 3, 4): []}, ["467..114..", "...*......", "..35..633."], {("*", 2, 3, 4): [("467", 1, 0, 3), ("35", 3, 2, 4)]}],
        [{("*", 2, 3, 4): []}, ["467..114..", "...*......", "......633."], {("*", 2, 3, 4): [("467", 1, 0, 3)]}],
    ]
)
def test_add_numbers_in_gears(gear: Dict[Tuple[str | int], List], mock_lines: List[str], expected_dict: Dict[Tuple[str | int], List[Tuple[str | int]]]) -> None:
    """
    Test add_numbers_in_gears function

    Parameters
    ----------
    gear : Dict[Tuple[str  |  int], List]
        Dictionary with gears.
    mock_lines : List[str]
        Mock upper, mid and lower lines.
    expected_dict : Dict[Tuple[str  |  int], List[Tuple[str  |  int]]]
        Expected dictionary with gears.
    """
    for coordinate in gear:
        with mock.patch(
            "day_03.gear_ratios.DATA_PATH", new="day_03/test_data"
            ), mock.patch.object(
                linecache, "getline"
                ) as mock_getline:
            mock_responses = {
                ("day_03/test_data", coordinate[1] - 1): mock_lines[0],
                ("day_03/test_data", coordinate[1]): mock_lines[1],
                ("day_03/test_data", coordinate[1] + 1): mock_lines[2]
            }
            mock_getline.side_effect = lambda filename, lineno: mock_responses.get((filename, lineno))
            test_gear = add_numbers_in_gears(gear)

            assert test_gear == expected_dict


@pytest.mark.parametrize(
    "numbers, expected_return",
    [
        [[("467", 1, 0, 3), ("35", 3, 2, 4)], 16345],
        [[("467", 1, 0, 3)], 0],
    ]
)
def test_extract_gears(numbers: List[Tuple[str | int]], expected_return: int) -> None:
    """
    Test extract_gears function

    Parameters
    ----------
    numbers : List[Tuple[str  |  int]]
        Numbers in gear.
    expected_return : int
        Expected number of gears.
    """
    assert extract_gears(numbers) == expected_return
