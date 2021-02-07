import pandas


# TODO 1. Create a dictionary in this format:
nato_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_alphabet = {
    row.letter: row.code for (index, row) in nato_alphabet.iterrows()
}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_word = input("Enter a word: ").upper()
answer = [
    phonetic_alphabet[letter] for letter in user_word
]
print(answer)
