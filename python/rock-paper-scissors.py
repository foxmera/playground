# By foxmera (MT Fischer), February 2023
#
# ROCK PAPER SCISSORS TERMINAL GAME
#

from random import randint

options = ["r", "p", "s"]
wins = ["rs", "pr", "sp"]
win_message = {
    "r": "Rock crushes Scissors.",
    "p": "Paper covers Rock.",
    "s": "Scissors cut Paper.",
}


def play():
    # assign a random play to the computer
    computer = options[randint(0, 2)]

    player = input("Rock, Paper, Scissors? r/p/s ")

    if player not in options:
        print("That's not a valid play. Check your spelling!")
        play()
        return

    print("Player:   " + player)
    print("Computer: " + computer)

    if player == computer:
        print("Tie!")
        play()
        return

    game = player + computer

    if game in wins:
        print("You win!", win_message[player])
    else:
        print("You lose!", win_message[computer])

    play()


play()
