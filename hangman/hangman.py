import re

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

def detect_special_characer(pass_string): 
    regex= re.compile('[@_!#$%^&*()<>?/\|}{~:]') 
    if(regex.search(pass_string) == None): 
        res = True
    else: 
        res = False
    return(res)

def check_valid_input(letter_guessed, old_letters_guessed, secret):
    '''
    Function that checks user input and  print error  messages for each case.
    :param letter_guessed: user input of a char
    :type letter_guessed: str
    :return: True/False
    :rtype: bool
    '''

    if len(letter_guessed) == 1  and detect_special_characer(letter_guessed) and (letter_guessed  not in old_letters_guessed) and (letter_guessed in secret):
        return True
    else:
        return False

def try_update_letter_guessed(letter_guessed, old_letters_guessed, secret):
    '''
    Function that ...
    :param 
    :type ...: ...
    :return: 
    :rtype: 
    '''
    word = ''
    ordered_old_letters_guessed = sorted(old_letters_guessed, key=str.casefold)

    if check_valid_input(letter_guessed, old_letters_guessed, secret) == False:
        old_letters_guessed.append(letter_guessed)
        print('X')
        for char in ordered_old_letters_guessed:
            word = char + ' -> '
            print(word, end = '')
        return False
    else:
        old_letters_guessed.append(letter_guessed)
        return True

def check_win(secret_word, old_letters_guessed):
    '''
    Function that ...
    :param 
    :type ...: ...
    :return: 
    :rtype: 
    '''
    for char in secret_word:
        if char in old_letters_guessed:
            continue
        else:
            return False
    return True

def choose_word(file_path, index):
    '''
    Function that ...
    :param 
    :type ...: ...
    :return: 
    :rtype: 
    '''
    with open(file_path, "r") as words_file:
        words = sorted(words_file.read().split())
        return (words[index])

def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                x-------x
                |       |
                |       0
                |      /|\\
                |      / \\
                |
                """,
                # head, torso, both arms, and one leg
                """
                x-------x
                |       |
                |       0
                |      /|\\
                |      /
                |
                """,
                # head, torso, and both arms
                """
                x-------x
                |       |
                |       0
                |      /|\\
                |
                |
                """,
                # head, torso, and one arm
                """
                x-------x
                |       |
                |       0
                |       |
                |
                |
                """,
                # head and torso
                """
                x-------x
                |       |
                |       0
                |
                |
                |
                """,
                # head
                """
                x-------x
                |
                |
                |
                |
                |
                """,
                # initial empty state
                """
                x-------x
                """
    ]
    return stages[tries]

def show_hidden_word(secret_word, old_letters_guessed):
    '''
    Function that ...
    :param 
    :type ...: ...
    :return: 
    :rtype: 
    '''
    word = ''
    for char in secret_word:
        if char in old_letters_guessed:
            word = word + char + ' '
        else:
            word = word + '_ '
    return word

def welcome_print(max_tries):
    HANGMAN_ASCII_ART = '''
    _    _                                      
    | |  | |                                      
    | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __ 
    |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
    | |  | | (_| | | | | (_| | | | | | | (_| | | | |
    |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/  |                      
                        |___/         
    '''
    MAX_TRIES = max_tries
    print(HANGMAN_ASCII_ART+ "\n")
    print('Max number of tries is:',MAX_TRIES)

def main():

    play()


if __name__ == '__main__':
    main()
