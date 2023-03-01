# By foxmera (MT Fischer), February 2023
# 
# HANGMAN TERMINAL GAME IN PYTHON
#


from nltk.corpus import words
import random


# game parameters
def init():
    global word
    global placeholder
    global already_guessed
    global error_count
    global limit
    global guesses_remaining

    word_list = words.words()
    word = random.choice(word_list).upper()

    placeholder = "_" * len(word)
    already_guessed = []
    error_count = 0
    limit = 5
    guesses_remaining = limit - error_count
    play()


# the actual gameplay
def play():
    global error_count
    global placeholder
    global word
    global already_guessed
    global continue_playing
    global guess

    guess = input("This is your word: " + display + " Enter your guess:\n")
    guess = guess.strip().upper()

    # TODO: handle invalid input
    # TODO: handle already guessed input

    already_guessed.extend([guess])

    # reveal characters if present
    indexes = find_indexes()
    if indexes:
        right_guess(indexes)
    else:
        wrong_guess()

    if error_count == limit:
        show_game_over()
        ask_for_replay()
    else:
        play()


def find_indexes():
    characters = list(word)
    length = len(characters)
    indexes = []
    i = 0
    while i < length:
        if guess == characters[i]:
            indexes.append(i)
        i += 1
    return indexes


def right_guess(indexes):
    global placeholder

def wrong_guess():
    global error_count

# loop to restart or exit the game after the first round ends
def ask_for_replay():
    global continue_playing

    continue_playing = input("Do you want to play again? y/n\n")

    if continue_playing == "y":
        print("\nCOOLIO! New round...\n")
        init()
    else:
        print("Bye! :*")
        exit()


init()
