"""EX07 -- Dictionary Functions: Unit Test Functions."""

__author__ = "730471018"

from exercises.ex07.dictionary import invert, favorite_color, count
import pytest


def test_invert_1() -> None:
    """Ensures that single character str keys and values are inverted."""
    items: dict[str, str] = {'a': 'b', 'c': 'd', 'e': 'f'}
    assert invert(items) == {'b': 'a', 'd': 'c', 'f': 'e'}


def test_invert_2() -> None: 
    """Ensures that multi character str keys and values are inverted."""
    items: dict[str, str] = {'steve': 'jobs', 'sundar': 'pichai', 'kris': 'jordan'}
    assert invert(items) == {'jobs': 'steve', 'pichai': 'sundar', 'jordan': 'kris'}


def test_invert_edge() -> None:
    """Ensures that empty list is returned if nothing is inputted."""
    items: dict[str, str] = {}
    assert invert(items) == {}


def test_favorite_color_1() -> None:
    """Ensures that between 2 colors with one appearing twice, the color appearing most is returned."""
    items: dict[str, str] = {'Bob': 'pink', 'Michael': 'orange', 'Ethan': 'pink'}
    assert favorite_color(items) == "pink"


def test_favorite_color_2() -> None:
    """Ensures that between 4 colors with one appearing twice, the color appearing most is returned."""
    items: dict[str, str] = {'Bob': 'pink', 'Michael': 'orange', 'Ethan': 'blue', 'Amanda': 'orange', 'Michelle': 'yellow'}
    assert favorite_color(items) == "orange"


def test_favorite_color_edge() -> None:
    """Ensures that between 2 colors that appear with equal frequencies, the first one listed is returned."""
    items: dict[str, str] = {'Bob': 'pink', 'Michael': 'orange', 'Ethan': 'orange', 'Amanda': 'pink', 'Michelle': 'yellow'}
    assert favorite_color(items) == "pink"


def test_count_1() -> None:
    """Ensures that in a list of 3 things with one appearing twice, the correct counts are returned."""
    items: list[str] = ["biology", "chemistry", "biology"]
    assert count(items) == {'biology': 2, 'chemistry': 1}


def test_count_2() -> None:
    """Ensures that in a list of 5 things with one appearing twice, the correct counts are returned."""
    items: list[str] = ["biology", "chemistry", "biology", "physics", "psychology"]
    assert count(items) == {'biology': 2, 'chemistry': 1, 'physics': 1, 'psychology': 1}


def test_count_edge() -> None:
    """Ensures if an empty list is given, an empty output is returned."""
    items: list[str] = []
    assert count(items) == {}


with pytest.raises(KeyError):
    my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
    invert(my_dictionary)