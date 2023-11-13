# By foxmerald, February 2023
#
# ROCK PAPER SCISSORS TERMINAL GAME
#

from random import randint


def init():
    global options
    global wins
    global win_message
    global name

    options = ("r", "p", "s")
    wins = ("rs", "pr", "sp")
    win_message = {
        "r": "Rock crushes Scissors.",
        "p": "Paper covers Rock.",
        "s": "Scissors cut Paper.",
    }
    name = {
        "r": "Rock",
        "p": "Paper",
        "s": "Scissors",
    }

    print(
        "WELCOME TO THIS GAME!\n"
        + "Choose one of three symbols: a rock, paper, or scissors.\n"
        + "A rock beats scissors by crushing them, scissors beat paper by cutting it, and paper beats rock by covering it.\n"
        + "Type 'x' to exit the game.\n"
    )

    play()


def play():
    # assign a random play to the computer
    computer = options[randint(0, 2)]

    player = input("Rock, Paper, Scissors? r/p/s ")

    if player == "x":
        print("Bye! :*")
        exit()

    if player not in options:
        print("That's not a valid play. Check your spelling!")
        return play()

    print("Player:   " + name[player])
    print("Computer: " + name[computer])

    if player == computer:
        print("Tie!")
        return play()

    game = player + computer

    if game in wins:
        print("You win!", win_message[player])
    else:
        print("You lose!", win_message[computer])

    play()


init()
