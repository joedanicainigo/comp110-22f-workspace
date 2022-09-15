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

def emojified(guess_word: str, secret_word: str) -> str:
    """Returns emojis that relates accuracy of guess to inputted secret word."""
    assert len(guess_word) == len(secret_word)
    box_emojis: str = ""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    idx: int = 0
    while idx < len(secret_word): 
        if contains_char(secret_word, guess_word[idx]) == False:
            box_emojis += WHITE_BOX
        else:
            if secret_word[idx] == guess_word[idx]:
                box_emojis += GREEN_BOX
            else: 
                box_emojis += YELLOW_BOX
        idx += 1
    return(box_emojis)

def input_guess(expected_guess_length: int) -> int:
    """Ensures guess matches the inputed expected length, and if not, prompts user to input new guess."""
    word_guess: str = input(f"Enter a {expected_guess_length} character word: ")
    while len(word_guess) != expected_guess_length:
        word_guess = input(f"That wasn't {expected_guess_length} chars! Try again: ")
    return(word_guess)

def main() -> None:
    """The entrypoint of the program and main game loops."""
    secret: str = "codes"
    guess: str = ""
    turns: int = 1
    win: bool = False
    while turns <= 6 and win == False:
        print(f"=== Turn {turns}/6 ===")
        guess = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            win = True
            print(f"You won in {turns}/6 turns!")
        else:
            if turns < 6:
                turns += 1
            else:
                print(f"X/6 - Sorry, try again tomorrow!")
                exit()