from string import ascii_letters
import re

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


# a = 'a'
# b = ['c', 'v', 'b']

# print(check_valid_input(a, b))