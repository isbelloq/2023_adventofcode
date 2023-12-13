"""Unit test for Day 4: Scratchcards"""

import pytest

from day_04.scratchcards import data_parser


@pytest.mark.parametrize(
    "input_data, expected_power",
    [
        ["Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53", 3],
        ["Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11", None]
    ]
)
def test_data_parser(input_data: str, expected_power: int) -> None:
    """
    Test data_parser function.

    Parameters
    ----------
    input : str
        Input string.
    expected_power : int
        Expected power.
    """
    power = data_parser(input_data)
    if power:
        assert isinstance(power, int)
        assert power == expected_power
