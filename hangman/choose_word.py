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