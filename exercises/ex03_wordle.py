"""EX03 - Structured Wordle - Wordle with multiple chances."""

__author__ = "730471018"
def contains_char(search: str, character: str) -> bool:
    """Searches inputted search word for inputted character."""
    assert len(character) == 1
    i: int = 0
    while i < len(search):
        if character == search[i]: 
            return True
            i += 1
    return False 
