"""Day 1: Trecuchet?!"""

from typing import Generator


def calibration_value_found(data: str) -> int:
    """
    Return the combinig the first digit and the last digit

    Parameters
    ----------
    data : str
        Input data

    Returns
    -------
    int
        Single two-digit number
    """

    calibration_value = ""
    # Extract first element
    for element in data:
        if element.isdigit():
            calibration_value += element
            break

    # Extract las element
    for element in data[::-1]:
        if element.isdigit():
            calibration_value += element
            break

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
    # Read data
    DATA_PATH = "day_01/data"
    sum_calibration_value = sum(map(calibration_value_found, data_reader(DATA_PATH)))
    print(sum_calibration_value)
