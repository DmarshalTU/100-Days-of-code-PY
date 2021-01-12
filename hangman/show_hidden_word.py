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