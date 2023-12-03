"""Unint test for Day 1: Trecuchet?!"""

from typing import Dict, List, Tuple

import pytest

from day_02.cube_conundrum import data_parse, detect_possible_games


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
    data_id = detect_possible_games(data)
    assert isinstance(data_id, int)
    assert data_id == expected_data_id
