"""Day 5: If You Give A Seed A Fertilizer"""

import argparse
from typing import List, Tuple


def step_source_destination(position: int, destination: int, source: int, range_length: int) -> int:
    """
    Return the position of the seed after the step.

    Parameters
    ----------
    position : int
        Actual position of the seed.
    destination : int
        Initial position of the seed.
    source : int
        Initial position of the source.
    range_length : int
        Length of the range.

    Returns
    -------
    int
        New position of the seed after the step.
    """
    if (position >= source) and (position < source + range_length):
        index_length = position - source
        return destination + index_length
    else:
        return position


def data_parser(data: List[str]) -> Tuple[List[int], List[List[str]]]:
    """
    Parse data and return the seeds and steps.

    Parameters
    ----------
    data : List[str]
        Data to parse.

    Returns
    -------
    Tuple[List[int], List[List[str]]]
        Seeds and steps.
    """
    data_split = data.split("\n\n")
    data_split = [*map(lambda x: x.split(":")[1], data_split)]
    seeds = [*map(int, data_split[0].split())]
    steps = [*map(lambda x: x.strip().split("\n"), data_split[1:])]
    for i, step in enumerate(steps):
        steps[i] = [*map(lambda x: x.split(), step)]

    return seeds, steps


def data_reader(path: str) -> str:
    """
    Read data from file

    Parameters
    ----------
    path : str
        Data path

    Returns
    -------
    str
        Data
    """
    with open(path, 'r') as file:
        return file.read()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Day 5: If You Give A Seed A Fertilizer")
    parser.add_argument("--test", help="If is True, use test data", action="store_true")

    args = parser.parse_args()

    DATA_PATH = "day_05/test_data" if args.test else "day_05/data"
    input_data = data_reader(DATA_PATH)
    seeds, steps = data_parser(input_data)

    last_position = {seed: seed for seed in seeds}

    for seed in last_position:
        for step in steps:
            for sub_step in step:
                current_position = last_position[seed]
                last_position[seed] = step_source_destination(current_position, *map(int, sub_step))
                if current_position != last_position[seed]:
                    break

    print(min(last_position.values()))
