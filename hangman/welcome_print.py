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