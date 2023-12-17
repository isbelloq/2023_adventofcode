"""Unit test for Day 5: If You Give A Seed A Fertilizer"""

import pytest

from day_05.if_you_give_a_seed_a_fertilizer import step_source_destination, data_parser


@pytest.mark.parametrize(
        "position, destination, source, range_length, expected_position",
        [
            [79, 50, 98, 2, 79],
            [79, 52, 50, 48, 81]
        ]
)
def test_step_source_destination(position: int, destination: int, source: int, range_length: int, expected_position: int) -> None:
    """
    Test step_source_destination function.

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
    expected_position : int
        Expected position of the seed after the step.
    """
    new_position = step_source_destination(position, destination, source, range_length)
    assert isinstance(new_position, int)
    assert expected_position == new_position


def test_data_parser() -> None:
    """Test data_parser function."""
    data_test = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

    seeds, steps = data_parser(data_test)
    assert isinstance(seeds, list)
    assert isinstance(steps, list)
    assert len(steps) == 7
    for step in steps:
        assert isinstance(step, list)
        for step_item in step:
            assert len(step_item) == 3
            assert isinstance(step_item, list)
