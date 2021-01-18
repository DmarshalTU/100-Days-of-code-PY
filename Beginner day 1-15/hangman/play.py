from check_valid_input import *
from welcome_print import *
from display_hangman import *
from choose_word import *
from show_hidden_word import *
from try_update_letter_guessed import *
from check_win import *

def play():
    guessed_letters = []
    tries = 6

    print("Let's play Hangman!")
    print("\n")
    welcome_print(tries)

    word_completion = choose_word(input('Enter valid path to words file: \n>>> '), int(input('Enter the index of the word: \n>>> ')))

    while not tries == 0:
        guess = input("Please guess a letter: \n>>> ").lower()
        if try_update_letter_guessed(guess, guessed_letters, word_completion) == True:
            print("Good job,", guess, "is in the word!")
            print(show_hidden_word(word_completion, guessed_letters))
            if check_win(word_completion, guessed_letters) == True:
                print('You win!')
                break
        else:
            print(guess, " Not a valid guess.")
            print(show_hidden_word(word_completion, guessed_letters))
            print(display_hangman(tries))
            tries -= 1
    else:
        print(display_hangman(tries))
        print('You lose...')