"""Unint test for Day 2: Cube Conundrum"""

from typing import Dict, List, Tuple

import pytest

from day_02.cube_conundrum import data_parse, detect_possible_games, power_set_of_cubes


@pytest.mark.parametrize(
        "data, expected_parse",
        [
            ["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green", (1, [{"blue": 3, "red": 4}, {"red": 1, "green": 2, "blue": 6}, {"green": 2}])],
            ["Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue", (2, [{"blue": 1, "green": 2}, {"green": 3, "blue": 4, "red": 1}, {"green": 1, "blue": 1}])],
            ["Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red", (3, [{"green": 8, "blue": 6, "red": 20}, {"blue": 5, "red": 4, "green": 13}, {"green": 5, "red": 1}])],
            ["Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red", (4, [{"green": 1, "red": 3, "blue": 6}, {"green": 3, "red": 6}, {"green": 3, "blue": 15, "red": 14}])],
            ["Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green", (5, [{"red": 6, "blue": 1, "green": 3}, {"blue": 2, "red": 1, "green": 2}])],
        ]
)
def test_data_parse(data: str, expected_parse: Tuple[int, List[Dict[str, int]]]) -> None:
    """
    Test data_parse function

    Parameters
    ----------
    data : str
        Input data
    expected_parse : Tuple[int, List[Dict[str, int]]]
        Expected parse
    """
    parse = data_parse(data)
    assert isinstance(parse, tuple)
    assert isinstance(parse[0], int)
    assert isinstance(parse[1], list)
    for record in parse[1]:
        assert isinstance(record, dict)
    assert parse == expected_parse


@pytest.mark.parametrize(
    "data, expected_data_id",
    [
        [(1, [{"blue": 3, "red": 4}, {"red": 1, "green": 2, "blue": 6}, {"green": 2}]), 1],
        [(2, [{"blue": 1, "green": 2}, {"green": 3, "blue": 4, "red": 1}, {"green": 1, "blue": 1}]), 2],
        [(3, [{"green": 8, "blue": 6, "red": 20}, {"blue": 5, "red": 4, "green": 13}, {"green": 5, "red": 1}]), 0],
        [(4, [{"green": 1, "red": 3, "blue": 6}, {"green": 3, "red": 6}, {"green": 3, "blue": 15, "red": 14}]), 0],
        [(5, [{"red": 6, "blue": 1, "green": 3}, {"blue": 2, "red": 1, "green": 2}]), 5],
    ]
)
def test_detect_possible_games(data: Tuple[int, List[Dict[str, int]]], expected_data_id: int) -> None:
    """
    Test detect_possible_games function

    Parameters
    ----------
    data : Tuple[int, List[Dict[str, int]]]
        Input data
    expected_data_id : int
        Expected data id
    """
    data_id = detect_possible_games(data)
    assert isinstance(data_id, int)
    assert data_id == expected_data_id


@pytest.mark.parametrize(
        "data, expected_power",
        [
            [(1, [{"blue": 3, "red": 4}, {"red": 1, "green": 2, "blue": 6}, {"green": 2}]), 48],
            [(2, [{"blue": 1, "green": 2}, {"green": 3, "blue": 4, "red": 1}, {"green": 1, "blue": 1}]), 12],
            [(3, [{"green": 8, "blue": 6, "red": 20}, {"blue": 5, "red": 4, "green": 13}, {"green": 5, "red": 1}]), 1560],
            [(4, [{"green": 1, "red": 3, "blue": 6}, {"green": 3, "red": 6}, {"green": 3, "blue": 15, "red": 14}]), 630],
            [(5, [{"red": 6, "blue": 1, "green": 3}, {"blue": 2, "red": 1, "green": 2}]), 36],
        ]
)
def test_power_set_of_cubes(data: Tuple[int, List[Dict[str, int]]], expected_power: int) -> None:
    """
    Test power_set_of_cubes function

    Parameters
    ----------
    data : Tuple[int, List[Dict[str, int]]]
        Input data
    expected_power : int
        Expected power
    """
    power = power_set_of_cubes(data)
    assert isinstance(power, int)
    assert power == expected_power
