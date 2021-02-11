import pandas

nato_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_alphabet = {
    row.letter: row.code for (index, row) in nato_alphabet.iterrows()
}


def generate_phonetic():
    user_word = input("Enter a word: ").upper()

    try:
        answer = [
            phonetic_alphabet[letter] for letter in user_word
        ]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(answer)


generate_phonetic()
