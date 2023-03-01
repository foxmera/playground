# By foxmera (MT Fischer), February 2023
# 
# HANGMAN TERMINAL GAME IN PYTHON
#


from nltk.corpus import words
import random
import time


# game parameters
def init():
    global word
    global placeholder
    global already_guessed
    global error_count
    global limit
    global guesses_remaining
    global graphic

    word_list = words.words()
    word = random.choice(word_list).upper()

    placeholder = "_" * len(word)
    already_guessed = []
    error_count = 0
    limit = 5
    guesses_remaining = limit - error_count
    graphic = [
        "",
        "   _____ \n"
        + "  |      \n"
        + "  |      \n"
        + "  |      \n"
        + "  |      \n"
        + "  |      \n"
        + "  |      \n"
        + "__|__    \n",
        "   _____ \n"
        + "  |     |\n"
        + "  |     |\n"
        + "  |      \n"
        + "  |      \n"
        + "  |      \n"
        + "  |      \n"
        + "__|__    \n",
        "   _____ \n"
        + "  |     |\n"
        + "  |     |\n"
        + "  |     |\n"
        + "  |      \n"
        + "  |      \n"
        + "  |      \n"
        + "__|__    \n",
        "   _____ \n"
        + "  |     |\n"
        + "  |     |\n"
        + "  |     |\n"
        + "  |     O\n"
        + "  |      \n"
        + "  |      \n"
        + "__|__    \n",
        "   _____   \n"
        + "  |     |  \n"
        + "  |     |  \n"
        + "  |     |  \n"
        + "  |     O  \n"
        + "  |    /|\ \n"
        + "  |    / \ \n"
        + "__|__      \n",
    ]

    play()


# the actual gameplay
def play():
    global error_count
    global placeholder
    global word
    global already_guessed
    global guess

    if "_" not in placeholder:
        return show_success()

    guess = input("This is your word: " + placeholder + "\nEnter your guess:\n")
    guess = guess.strip().upper()

    if len(guess) != 1:
        print("<", guess, "> is not a valid input. Please try something else.\n")
        play()
        return

    if guess in already_guessed:
        print("Letter", guess, "was already picked. Please try something else.\n")
        play()
        return

    already_guessed.extend([guess])

    # reveal characters if present
    indexes = find_indexes()

    if indexes:
        right_guess(indexes)
    else:
        wrong_guess()

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

    for i in indexes:
        placeholder = placeholder[:i] + guess + placeholder[i + 1 :]


def wrong_guess():
    global error_count

    error_count += 1

    if error_count == limit:
        show_game_over()
        ask_for_replay()
        return

    print(graphic[error_count])
    print("Wrong guess.", str(limit - error_count), "guess/es remaining\n")


def show_game_over():
    print(graphic[5])
    print("Wrong guess. You are hanged!!!\n")
    print("The word was:", word)


def show_success():
    print("Yes, it's", word, "!")
    print("CONGRATS! YOU BEAT THE GAME :D")
    ask_for_replay()


# loop to restart or exit the game after the first round ends
def ask_for_replay():
    time.sleep(2)

    continue_playing = input("Do you want to play again? y/n\n")

    if continue_playing == "y":
        print("\nCOOLIO! New round...\n")
        init()
    else:
        print("Bye! :*")
        exit()


init()
