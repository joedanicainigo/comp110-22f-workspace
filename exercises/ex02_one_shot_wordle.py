"""EX02 - One Shot Wordle - Wordle reduced to one chance."""

__author__ = "730471018"
secret_word: str = "python"
guess: str = input(f"What is your {len(secret_word)}-letter guess? ")
"""Test to see whether guess has the same # of letters as secret word; if not ask for new guess."""
while len(guess) != len(secret_word):
    guess = input(f"That was not {len(secret_word)} letters! Try again: ")
i: int = 0
box_emojis: str = ""
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
"""Test to see whether guess's index matches secret word's index (green box)."""
"""If not, test whether guess's index matches any other index in the secret word (yellow box)."""
"""If guess's index is not found, a white box is inputted."""
while i < len(secret_word):
    if guess[i] == secret_word[i]:
        box_emojis += GREEN_BOX
    else:
        guess_existence: bool = False
        alternate_i: int = 0
        while guess_existence is not True and alternate_i < len(secret_word):
            if guess[i] == secret_word[alternate_i]:
                guess_existence = True
            else:
                alternate_i += 1
        if guess_existence is True:
            box_emojis += YELLOW_BOX
        else:
            box_emojis += WHITE_BOX
    i += 1
"""Print box emojis and phrase regarding whether guess matches secret word."""
print(box_emojis)
if guess == secret_word:
    print("Woo! You got it!")
else: 
    print("Not quite. Play again soon!")