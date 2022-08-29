"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730471018"
final_word = str = input("Enter a 5-character word: ")
if len(final_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
letter_guess = str = input("Enter a single character: ")
if len(letter_guess) != 1:
    print("Error: Character must be a single character.")
    exit()
instances_of_letter = int = 0
print("Searching for " + letter_guess + " in " + final_word)
if letter_guess == final_word[0]:
    print(letter_guess + " found at index 0")
    instances_of_letter = instances_of_letter + 1
if letter_guess == final_word[1]:
    print(letter_guess + " found at index 1")
    instances_of_letter = instances_of_letter + 1
if letter_guess == final_word[2]:
    print(letter_guess + " found at index 2")
    instances_of_letter = instances_of_letter + 1
if letter_guess == final_word[3]:
    print(letter_guess + " found at index 3")
    instances_of_letter = instances_of_letter + 1
if letter_guess == final_word[4]:
    print(letter_guess + " found at index 4")
    instances_of_letter = instances_of_letter + 1
if instances_of_letter == 0:
    print("No instances of " + letter_guess + " found in " + final_word)
else: 
    if instances_of_letter == 1:
        print("1 instance of " + letter_guess + " found in " + final_word)
    if instances_of_letter == 2: 
        print("2 instances of " + letter_guess + " found in " + final_word)
    if instances_of_letter == 3: 
        print("3 instances of " + letter_guess + " found in " + final_word)
    if instances_of_letter == 4: 
        print("4 instances of " + letter_guess + " found in " + final_word)
    if instances_of_letter == 5: 
        print("5 instances of " + letter_guess + " found in " + final_word)
