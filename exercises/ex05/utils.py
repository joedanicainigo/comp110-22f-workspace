"""EX05 - Building List Utility Functions -- Implementaiton of Function Skeletons."""

__author__ = "730471018"


def only_evens(numbers_list: list[int]) -> list[int]:
    """Only the even numbers from the original list will be returned as a new list of integers."""
    i: int = 0
    evens_list: list[int] = list()
    while i < len(numbers_list):
        if numbers_list[i] % 2 == 0:
            evens_list.append(numbers_list[i])
        i += 1
    return evens_list


def concat(first_list: list[int], second_list: list[int]) -> list[int]:
    """A new list should be generated with the integers of the first list followed by the integers of the second list."""
    concat_list: list[int] = list()
    i: int = 0
    while i < len(first_list):
        concat_list.append(first_list[i])
        i += 1
    idx: int = 0
    while idx < len(second_list):
        concat_list.append(second_list[idx])
        idx += 1
    return concat_list


def sub(integer_list: list[int], start_index: int, end_index: int) -> list[int]:
    """A subset of a given list of integers within a starting and ending index (not inclusive) will be returned."""
    sub_list: list[int] = list()
    if start_index < 0:
        start_index = 0
    if end_index > len(integer_list):
        end_index = len(integer_list)
    if len(integer_list) == 0 or start_index > len(integer_list) or end_index <= 0:
        return sub_list
    i: int = start_index
    while i >= start_index and i < end_index:
        sub_list.append(integer_list[i])
        i += 1
    return sub_list
