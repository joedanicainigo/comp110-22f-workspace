"""EC06 - Choose Your Own Adventure: Haunted House Hangout!"""

__author__ = "730471018"

points: int = 0
player: str = ""
# Defining emoji Unicodes as global variables to have easier readability
CLOWN: str = "\U0001F921"
GHOST: str = "\U0001F47B"
DEVIL: str = "\U0001F47A"
PUMPKIN: str = "\U0001F383"
GOBLIN: str = "\U0001F479"
SPIDER: str = "\U0001F577"
SCORPION: str = "\U0001F982"
ROCK: str = "\U0001FAA8"
BRICK: str = "\U0001F9F1"
COOKIE: str = "\U0001F36A"
CUPCAKE: str = "\U0001F370"
ALIEN: str = "\U0001F47D"
CAT: str = "\U0001F63C"
MONKEY: str = "\U0001F64A"
BEE: str = "\U0001F41D"
COCKROACH: str = "\U0001FAB3"
HOURGLASS: str = "\U000023F3"
FISH: str = "\U0001F41F"
COFFEE: str = "\U00002615"
TEA: str = "\U0001F375"


def main() -> None:
    """Main function that calls all the other functions for game."""
    global points
    global player
    greet()
    first_path()
    if points == 1:
        print("Lucky you, you have left the Haunted House! ")
        print(f"Adventure Points Earned: {points}")
    else:
        points = final_path(points)
        print(f"Adventure Points Earned: {points}")
        again: bool = True
        while again is True:
            reenter: str = input("You just realized you left your phone inside the Haunted House. Would you like to go in again, yes or no? ")
            if reenter == "no":
                points += 1
                print(f"Hope you enjoyed your adventure at the Haunted House, {player}!")
                again = False
            elif reenter == "yes":
                points += 1
                reenter_choice: str = input("Where do you want to start your adventure again to look for it: entrance, doors, or hallways? ")
                if reenter_choice == "entrance":
                    points += 1
                    first_path()
                elif reenter_choice == "doors":
                    points += 1
                    third_path_1(second_path_1())
                    points = final_path(points)
                elif reenter_choice == "hallways":
                    points += 1
                    from random import randint
                    door_number: int = randint(1, 3)
                    third_path_2("Door " + str(door_number))
                    points = final_path(points)
            print(f"Adventure Points Earned: {points}")
        
                
def greet() -> None:
    """Initial greeting and setting player name."""
    global player
    global GHOST
    print(f"Welcome to the Haunted House Hangout! \nYou are welcome to stay as long as you like, but you must escape before the clock strikes 12, or else... {GHOST}")
    player = input("What is the name of who dared venture here? ")
    print(f"Time to start your adventure, {player}! Don't say you weren't warned!!")


def first_path() -> None:
    """Player makes choice on which door to enter first."""
    global points
    global player
    print("You enter the dark house, hearing ominous noises surrounding you. You have two options: \ngo left\nor\ngo right\nor\nback out.")
    first_choice: str = input(f"Which do you choose, {player}? ")
    if first_choice == "go left":
        points += 4
        print(f"I wish you the best of luck, {player}.")
        third_path_1(second_path_1())
    elif first_choice == "go right":
        points += 3
        print(f"I wish you the best of luck, {player}.")
        third_path_2(second_path_2())
    elif first_choice == "back out":
        points += 1


def second_path_1() -> str:
    """Chose left: player makes choice on which path to enter second."""
    global points
    global player
    global DEVIL, PUMPKIN, GOBLIN, SPIDER, SCORPION, ROCK, BRICK, COOKIE, CUPCAKE
    print(f"You have made your way to the first set of doors. You are presented with 3 doors: \nDoor 1 has a masked man holding a bloody ax. {DEVIL}\nDoor 2 has a demon pumpkin ready to possess its next victim.{PUMPKIN}\nDoor 3 has shreaking goblins that love to jumpscare.{GOBLIN}\nWhich door do you choose, {player}?")
    second_choice_1: str = input("Choose your path by typing 'Door #': ")
    if second_choice_1 == "Door 1":
        points += 5
        print(f"Bold choice, {player}! You run as fast as you can with the murderer chasing behind you, and have to choose between 2 hallways. The black hallway is filled with spiders {SPIDER}, and the brown hallway is filled with scorpions {SCORPION}.")
    elif second_choice_1 == "Door 2":
        points += 3
        print(f"Daring choice, {player}! You trip the demon pumpkin, and as he falls to the floor, you take the chance to run to the 2 gates. The star gate leads to a path with falling, star-shaped rocks {ROCK}, and the square gate leads to a path with falling bricks {BRICK}.")
    elif second_choice_1 == "Door 3":
        points += 1
        print(f"Safe choice, {player}! You run past the ghosts with your hands against your ears, and you come across two tables with food, one of which you must consume for the locked door to open. The cookie table {COOKIE} makes you lose your sight for five minutes, while the cupcake table {CUPCAKE} makes you hallucinate for five minutes.")
    return second_choice_1


def third_path_1(choice: str) -> None:
    """Chose left: player makes a choice on which path to enter third."""
    global points
    global player
    third_choice_1: str = ""
    if choice == "Door 1":
        third_choice_1 = input("Which path do you choose: \nblack hallway\nor\nbrown hallway? \nChoose wisely, as you are in control of your own fate: ")
        if third_choice_1 == "black hallway":
            points += 3
            print("You squish the spiders and make it safely to the other side!")
        elif third_choice_1 == "brown hallway":
            points += 1
            print("You squish the scorpions and make it safely to the other side!")
    elif choice == "Door 2":
        third_choice_1 = input("Which path do you choose: \nstar gate\nor\nsquare gate? \nChoose wisely, as you are in control of your own fate: ")
        if third_choice_1 == "star gate":
            points += 3
            print("You dodge the falling rocks and manage to make it to safety!")
        elif third_choice_1 == "square gate":
            points += 1
            print("You dodge the falling bricks and manage to make it to safety!")
    elif choice == "Door 3":
        third_choice_1 = input("Which path do you choose: \ncookie table\nor\ncupcake table? \nChoose wisely, as you are in control of your own fate: ")
        if third_choice_1 == "cookie table":
            points += 3
            print("You stumble through the pathway, unable to see anything, finally finding the exit just as your eyesight returns!")
        elif third_choice_1 == "cupcake table":
            points += 1
            print("You stumble through the pathway, seeing weird figures, finnaly finding the exit just as your normal vision returns!")


def second_path_2() -> str:
    """Chose right: player makes choice on which path to enter second."""
    global points
    global player
    global ALIEN, CAT, MONKEY, BEE, COCKROACH, HOURGLASS, FISH, COFFEE, TEA
    print(f"You have made your way to the first set of doors. You are presented with 3 doors: \nDoor 1 has a human-eating alien. {ALIEN}\nDoor 2 has an evil cat that casts spells.{CAT}\nDoor 3 has flying monkeys with razorblade wings.{MONKEY}\nWhich door do you choose, {player}?")
    second_choice_2: str = input("Choose your path by typing 'Door #': ")
    if second_choice_2 == "Door 1":
        points += 5
        print(f"Bold choice, {player}! You run as fast as you can with the alien chasing behind you, and have to choose between 2 hallways. The yellow hallway is filled with bees {BEE}, and the orange hallway is filled with cockroaches {COCKROACH}.")
    elif second_choice_2 == "Door 2":
        points += 3
        print(f"Daring choice, {player}! You distract the evil cat with a yarn ball, and you take the chance to run to the 2 gates. The circle gate leads to a path with quicksand pit {HOURGLASS}, and the triangle gate has a river filled with piranhas {FISH}.")
    elif second_choice_2 == "Door 3":
        points += 1
        print(f"Safe choice, {player}! You run past the flying monkeys, and you come across two tables with drinks, one of which you must consume for the locked door to open. The coffee table {COFFEE} makes you lose coordination for five minutes, while the tea table {TEA} makes you dizzy for five minutes.")
    return second_choice_2


def third_path_2(choice: str) -> None:
    """Chose left: player makes a choice on which path to enter third."""
    global points
    global player
    third_choice_2: str = ""
    if choice == "Door 1":
        third_choice_2 = input("Which path do you choose: \nyellow hallway\nor\norange hallway? \nChoose wisely, as you are in control of your own fate: ")
        if third_choice_2 == "yellow hallway":
            points += 3
            print("You swat the bees and make it safely to the other side!")
        elif third_choice_2 == "orange hallway":
            points += 1
            print("You stomp on the cockroaches and make it safely to the other side!")
    elif choice == "Door 2":
        third_choice_2 = input("Which path do you choose: \ncircle gate\nor\ntriangle gate? \nChoose wisely, as you are in control of your own fate: ")
        if third_choice_2 == "circle gate":
            points += 3
            print("You speedwalk across the quicksand and manage to make it to safety!")
        elif third_choice_2 == "triangle gate":
            points += 1
            print("You quickly swam across the river and manage to make it to safety!")
    elif choice == "Door 3":
        third_choice_2 = input("Which path do you choose: \ncoffee table\nor\ntea table? \nChoose wisely, as you are in control of your own fate: ")
        if third_choice_2 == "coffee table":
            points += 3
            print("You stumble through the pathway, finally finding the exit just as your ability to move properly returns!")
        elif third_choice_2 == "tea table":
            points += 1
            print("You stumble through the pathway, unable to see, finnaly finding the exit just as your normal vision returns!")


def final_path(point_number: int) -> int:
    """Final game which leads to exit of game, or allows player to enter loop in main function to continue game."""
    global CLOWN
    print(f"You stumble into a brightly lit open room, and you look up to see a giant scary {CLOWN}. You must play a game with {CLOWN} to safely escape the Haunted House. {CLOWN} will choose a random number and you will choose a random number between 0 & 9, inclusive.")
    from random import randint
    clown_number: int = randint(1, 9)
    user_number: int = int(input("Now you choose a number between 1 and 9, inclusive: "))
    print(f"If the number you chose is greater than the number {CLOWN} chose, then you can escape.\nLet's determine your fate...")
    print(f"{CLOWN} said {clown_number}.")
    if user_number > clown_number: 
        print(f"Congrats, {player}. You have won against {CLOWN}!")
        point_number += 10
    else:
        print(f"Unfortunately, {player}, {CLOWN} once again has outsmarted the adventurer.")
        point_number += 5
    return point_number


if __name__ == "__main__":
    main()