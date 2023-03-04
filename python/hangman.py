# By foxmera (MT Fischer), February 2023
#
# HANGMAN TERMINAL GAME IN PYTHON
#


from nltk.corpus import words
import random
import time


# Setup method for the initial game play.
def init():
    global word
    global placeholder
    global already_guessed
    global error_count
    global max_guess_count
    global guesses_remaining
    global graphic

    word_list = words.words()
    word = random.choice(word_list).upper()

    placeholder = "." * len(word)
    already_guessed = []
    error_count = 0
    max_guess_count = 5
    guesses_remaining = max_guess_count - error_count
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

    print(
        "WELCOME TO HANGMAN!\n"
        + "The computer will choose a word and you try to find it out by guessing single letters.\n"
        + "Each incorrect guess brings you closer to being 'hanged' aka losing the game.\n"
        + "Typing in '?' lists all letters that were already guessed.\n"
    )

    play()


# This runs the actual game and is looped through until a win or game over.
def play():
    global guess

    if "." not in placeholder:
        return show_success()

    guess = input("This is your word: " + placeholder + "\nEnter your guess:\n")

    if guess == "?":
        print("\nAlready guessed:", already_guessed)
        return play()

    guess = guess.strip().upper()

    if len(guess) != 1:
        print("\n<", guess, "> is no valid input. Please try something else.\n")
        return play()

    if guess in already_guessed:
        print("\nLetter", guess, "was already picked. Please try something else.\n")
        return play()

    already_guessed.extend([guess])

    # Looking for positions of the guessed letter in the solution word.
    # On a right guess all occurences of "." in the placeholder are replaced
    # by the given letter. Should the guessed letter not be part of the word
    # another part of the hanged man is added.
    indexes = find_indexes()

    if indexes:
        right_guess(indexes)
    else:
        wrong_guess()

    play()


# Returns an array of integers that contain the position of all
# occurences of "." in the placeholder that shall later be replaced
# by the guessed letter.
def find_indexes():
    characters = list(word)
    indexes = []

    for i, char in enumerate(characters):
        if char == guess:
            indexes.append(i)

    return indexes


# A guess is considered right if the solution word contains at least one
# occurence of the guessed letter.
def right_guess(indexes):
    global placeholder

    for i in indexes:
        placeholder = placeholder[:i] + guess + placeholder[i + 1 :]


# A guess is considered wrong if the solution word doesn't contain the
# guessed letter. In case the maximum amount of guesses is reached,
# the game stops and shows the game over message.
def wrong_guess():
    global error_count

    error_count += 1

    if error_count == max_guess_count:
        show_game_over()
        ask_for_replay()
        return

    print(graphic[error_count])
    print("\nWrong guess.", str(max_guess_count - error_count), "guess/es remaining.")


def show_game_over():
    print(graphic[5])
    print("\nWrong guess. You are hanged!!!")
    print("The word was:", word)


def show_success():
    print("\nCorrect, it's", word, "!")
    print("CONGRATS! YOU BEAT THE GAME :D")
    ask_for_replay()


# Option for the player to restart or exit the game after a win or loose.
def ask_for_replay():
    time.sleep(2)

    continue_playing = input("Do you want to play again? y/n\n")

    if continue_playing == "y":
        print("\nCOOLIO! New round...\n")
        init()
    else:
        print("\nBye! :*")
        exit()


init()
