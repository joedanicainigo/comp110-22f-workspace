"""EX04 - 'list' Utility Functions -- Creating functions to compare lists."""

__author__ = "730471018"


def all(integer_list: list[int], given_integer: int) -> bool:
    """Check whether a given integer is in a list of integers."""
    if len(integer_list) == 0:
        return False
    i: int = 0
    while i < len(integer_list):
        if integer_list[i] != given_integer:
            return False
        i += 1
    return True
    return all
    

def max(int_list: list[int]) -> int:
    """Given an inputted list of integers, the largest integer will be returned."""
    if len(int_list) == 0:
        raise ValueError("max() arg is an empty List")
    else:
        idx: int = 1
        max_value: int = int_list[0]
        while idx < len(int_list):
            if int_list[idx] > max_value:
                max_value = int_list[idx]
            idx += 1
    return max_value


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Checks if the elements and the order they are in are identical between 2 lists of integers."""
    if len(list_1) != len(list_2):
        return False
    if len(list_1) == 0 and len(list_2) == 0:
        return True
    else: 
        if len(list_1) == 0 or len(list_2) == 0:
            return False
    index_1: int = 0
    index_2: int = 0
    while index_1 < len(list_1) and index_2 < len(list_2):
        if list_1[index_1] != list_2[index_2]:
            return False
        index_1 += 1
        index_2 += 1
    return True
    return is_equal

    