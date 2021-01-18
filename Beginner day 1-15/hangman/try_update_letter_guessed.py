from check_valid_input import *

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