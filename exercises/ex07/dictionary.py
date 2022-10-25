"""EX07 -- Dictionary Functions: Implementation of Function Skeletons."""

__author__ = "730471018"


def invert(dictionary_og: dict[str, str]) -> dict[str, str]:
    """Inverts key and value strings in original dictionary and returns a new dictionary with inverted items."""
    key_list: list = list()
    values_list: list = list()
    for key in dictionary_og:
        key_list.append(key)
    for key in dictionary_og:
        values_list.append(dictionary_og[key])
    idx: int = 0
    repeat: bool = False
    index: int = 1
    while index < len(values_list) and repeat is False:
        if values_list[idx] == values_list[index]:
            repeat = True
            raise KeyError("You have duplicate values in the values list of your original dictionary")
        index += 1        
    dictionary_new: dict[str, str] = {}
    i: int = 0
    while i < len(key_list):
        dictionary_new[values_list[i]] = key_list[i]
        i += 1
    return dictionary_new


def favorite_color(colors: dict[str, str]) -> str:
    """Counts the frequency of colors listed in dictionary's values, and returns color with the greatest frequency."""
    color_list: list = list()
    for key in colors:
        color_list.append(colors[key])
    fav_color: str = str()
    if len(color_list) == 0:
        return fav_color
    i: int = 0
    max_count: int = 0
    while i < len(color_list):
        color: str = color_list[i]
        idx: int = 0
        current_count: int = 0
        while idx < len(color_list):
            if color == color_list[idx]:
                current_count += 1
            idx += 1
        if current_count > max_count:
            max_count = current_count
            fav_color = color
        i += 1
    return fav_color


def count(input_list: list[str]) -> dict[str, int]:
    """Counts the frequency of each unique item in a list and returns the unique item and its frequency in a dictionary."""
    dictionary_count: dict[str, int] = {}
    i: int = 0
    while i < len(input_list):
        if input_list[i] in dictionary_count:
            dictionary_count[input_list[i]] += 1
        else:
            dictionary_count[input_list[i]] = 1
        i += 1
    return dictionary_count
    
