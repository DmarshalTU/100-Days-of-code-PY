
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

