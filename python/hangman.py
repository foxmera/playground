# By foxmera (MT Fischer), February 2023
# 
# HANGMAN TERMINAL GAME IN PYTHON
#


from nltk.corpus import words
import random


# game parameters
def main():
    global word
    global display
    global already_guessed
    global length
    global continue_playing
    global count

    word_list = words.words()
    word = random.choice(word_list).upper()
    length = len(word)
    display = "_" * length
    already_guessed = []
    count = 0


# the actual gameplay
def play_hangman():
    global count
    global display
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
        for i in indexes:
            display = display[:i] + guess + display[i + 1 :]
    else:
        extend_hangman()


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


def extend_hangman():
    global count


# loop to restart or exit the game after the first round ends
def play_loop():
    global continue_playing

    continue_playing = input("Do you want to play again? y/n\n")

    while continue_playing == "y":
        main()
    else:
        print("Bye! :*")
        exit()


main()
play_hangman()
