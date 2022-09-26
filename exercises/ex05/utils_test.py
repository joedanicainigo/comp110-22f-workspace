"""EX05 - Building List Utility Functions -- Unit Test Functions."""

__author__ = "730471018"

from utils import only_evens, sub, concat

# tests for only_evens

def test_only_evens_even_items_1() -> None:
    """Ensures that the one even number in the list (2) is identified and added to the new list."""
    items: list[int] = [1, 2, 3]
    assert only_evens(items) == [2]

def test_only_evens_even_items_2() -> None:
    """Ensures that in a list of all even numbers, all of the numbers are added to the new list."""
    items: list[int] = [4, 4, 4]
    assert only_evens(items) == [4, 4, 4]

def test_only_evens_even_items_3() -> None:
    """Ensures that in a longer sequence, the 2 even numbers (single and double-digit) are identified and added to the new list."""
    items: list[int] = [1, 3, 8, 10, 5]
    assert only_evens(items) == [8, 10]

def test_only_evens_no_even() -> None:
    """Ensures that when no even numbers are present, an empty list is generated (edge case)."""
    items: list[int] = [1, 5, 3]
    assert only_evens(items) == []

# tests for concat

def test_concat_empty_list_1() -> None:
    """If first list is empty, continues to append integers of second list w/o modification (edge case)."""
    list_1: list[int] = list()
    list_2: list[int] = [1, 2, 3]
    assert concat(list_1, list_2) == [1, 2, 3]

def test_concat_empty_list_2() -> None:
    """If second list is empty, continues to append integers of first list w/o modification (edge case)."""
    list_1: list[int] = [4, 5, 6]
    list_2: list[int] = list()
    assert concat(list_1, list_2) == [4, 5, 6]

def test_concat_equal_list() -> None:
    """If lists of equal lengths are given, new list is made without modifications to integers."""
    list_1: list[int] = [7, 8, 9]
    list_2: list[int] = [10, 11, 12]
    assert concat(list_1, list_2) == [7, 8, 9, 10, 11, 12]

def test_concat_unequal_list() -> None:
    """If lists of unequal lengths are given, new list is made without modifications to integers."""
    list_1: list[int] = [10, 11, 12, 13]
    list_2: list[int] = [7, 8, 9]
    assert concat(list_1, list_2) == [10, 11, 12, 13, 7, 8, 9]

# tests for sub

def test_sub_same_index() -> None:
    """If start and end indexes are the same, an empty list should be returned (edge case)."""
    int_list: list[int] = [1, 2, 3, 4]
    start_i: int = 2
    end_i: int = 2
    assert sub(int_list, start_i, end_i) == []

def test_sub_empty_list() -> None:
    """Ensures empty list is returned if list has no values."""
    int_list: list[int] = []
    start_i: int = 0
    end_i: int = 0
    assert sub(int_list, start_i, end_i) == []

def test_sub_incorrect_indexes() -> None:
    """Ensures that when incorrect start and end indexes are given, they are fixed to result in all values of the list being returned."""
    int_list: list[int] = [1, 2, 3, 4]
    start_i: int = -1
    end_i: int = 5
    assert sub(int_list, start_i, end_i) == [1, 2, 3, 4]

def test_sub_greater_start() -> None:
    """Ensures that if start index is greater than the length of the list, an empty list is returned."""
    int_list: list[int] = [1, 2, 3, 4]
    start_i: int = 5
    end_i: int = 2
    assert sub(int_list, start_i, end_i) == []

def test_sub_zero_end() -> None:
    """Ensures that if end index is at most 0, an empty list is returned."""
    int_list: list[int] = [1, 2, 3, 4]
    start_i: int = 2
    end_i: int = 0
    assert sub(int_list, start_i, end_i) == []

def test_sub_values_small() -> None:
    """Ensures that for a small list of numbers, the proper subset is given."""
    int_list: list[int] = [1, 2, 3, 4]
    start_i: int = 1
    end_i: int = 3
    assert sub(int_list, start_i, end_i) == [2, 3]

def test_sub_values_large() -> None:
    """Ensures that for a large list of numbers, the proper subset is given."""
    int_list: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    start_i: int = 2
    end_i: int = 8
    assert sub(int_list, start_i, end_i) == [3, 4, 5, 6, 7, 8]
