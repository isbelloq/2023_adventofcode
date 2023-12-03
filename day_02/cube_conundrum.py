"""Day 2: Cube Conundrum"""

import argparse
from typing import Dict, Generator, Tuple, List

MAX_CUBE_CONUNDRUM = {
    "red": 12,
    "green": 13,
    "blue": 14
}


def data_parse(data: str) -> Tuple[int, List[Dict[str, int]]]:
    """
    Parse data to get game id and records

    Parameters
    ----------
    data : str
        Input data

    Returns
    -------
    Tuple[int, List[Dict[str, int]]]
        Game id and records
    """
    game, games_records = data.split(": ")
    games_records = games_records.split("; ")
    for i, game_record in enumerate(games_records):
        records = game_record.split(", ")
        games_records[i] = {record.split()[1]: int(record.split()[0]) for record in records}

    return int(game.split()[1]), games_records


def detect_possible_games(data: Tuple[int, List[Dict[str, int]]]) -> int:
    """
    Detect if is possible the game base on number of cubes

    Parameters
    ----------
    data : Tuple[int, List[Dict[str, int]]]
        Game id and records

    Returns
    -------
    int
        Game id if is possible, 0 otherwise
    """
    data_id = data[0]

    for game_record in data[1]:
        for color in game_record:
            if game_record[color] > MAX_CUBE_CONUNDRUM[color]:
                data_id = 0
                break
    return data_id


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
        for line in file.readlines():
            yield line


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Day 2: Cube Conundrum")
    parser.add_argument("--test", help="If is True, use test data", action="store_true")
    args = parser.parse_args()

    DATA_PATH = "day_02/test_data" if args.test else "day_02/data"

    records_parser = map(data_parse, data_reader(DATA_PATH))
    sum_id_possible_games = sum(map(detect_possible_games, records_parser))

    print(sum_id_possible_games)
