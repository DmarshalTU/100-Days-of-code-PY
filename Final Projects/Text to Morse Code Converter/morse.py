class Morse:
    """
                A simple class that return morse code like string.alpha/numeric kinda style
                and can encode or decode morse

                morse_test = Morse()
                print(morse_test.morse_letters)
                '.-    -...    -.-.    -..    .    ..-. etc'

                print(morse_test.morse_digits)
                '.----    ..---    ...--    ....-    ..... etc'

                print(morse_test.morse_punctuation)
                '.-.-.-    --..--    ..--..    -.-.--'

                print(morse_test.morse_table)
                '{'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..' etc'

                print(morse_test.encode_morse("den"))
                '-.. . -. '
                print(morse_test.decode_morse('-.. . -.'))
                'den'

    """

    def __init__(self):
        self.morse_letters = '    '.join(
            [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..",
             "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-",
             "-.--", "--.."])

        self.morse_digits = '    '.join(
            [".----", "..---", "...--", "....-", ".....", "-....", "--...", "---..", "----.",
             "-----"])

        self.morse_punctuation = '    '.join([".-.-.-", "--..--", "..--..", "-.-.--"])

        self.morse_table = {"a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.",
                            "h": "....",
                            "i": "..", "j": ".---",
                            "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---", "p": ".--.", "q": "--.-",
                            "r": ".-.",
                            "s": "...", "t": "-",
                            "u": "..-", "v": "...-", "w": ".--", "x": "-..-", "y": "-.--", "z": "--..", "1": ".----",
                            "2": "..---",
                            "3": "...--", "4": "....-",
                            "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.", "0": "-----",
                            ".": ".-.-.-",
                            ",": "--..--", "?": "..--..", "!": "-.-.--"}

    def print_table(self):
        for k, v in self.morse_table.items():
            label = v
            print("{:<8} {:<15}".format(k, label))

    def encode_morse(self, string):
        """
                Translates text to morse code

                Accepts:
                    text (str): A string of text to translate

                Returns:
                    str: A string translated to Morse code
        """
        string = string.lower().split()
        morse_encoded = ""
        for letter in string:
            for char in letter:
                morse_encoded += self.morse_table[char]
                morse_encoded += " "
            morse_encoded += "       "
        return morse_encoded

    def decode_morse(self, string):
        """
                Translates morse code to text

                Accepts:
                    morse (str): A string of morse code to translate

                Returns:
                    str: A translated string of text
                """

        string += ' '

        decipher = ''
        citext = ''
        for letter in string:
            if letter != ' ':
                i = 0
                citext += letter

            else:
                i += 1
                if i == 2:
                    decipher += ' '
                else:
                    decipher += list(self.morse_table.keys())[list(self.morse_table
                                                                   .values()).index(citext)]
                    citext = ''

        return decipher
