"""Unint test for Day 1: Trecuchet?!"""

import pytest

from day_01.trebuchet import calibration_value_found


@pytest.mark.parametrize(
    "data, expected_calibration_value",
    [
        ["1abc2", 12],
        ["pqr3stu8vwx", 38],
        ["a1b2c3d4e5f", 15],
        ["treb7uchet", 77]
    ]
)
def test_calibration_value_found(data: str, expected_calibration_value: int) -> None:
    """
    Test calibration_value_found function

    Parameters
    ----------
    data : str
        Input data
    calibration_value : int
        Single two-digit number
    """

    calibration_value = calibration_value_found(data)

    assert isinstance(calibration_value, int)
    assert (calibration_value >= 10) & (calibration_value <= 99)
    assert calibration_value == expected_calibration_value
