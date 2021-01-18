# Ceaser cipher
import string


def ceaser(text, shift, direction):
    encrypted_text = ''
    if direction == "d":
        shift *= -1
    for letter in text:
        if letter in letters:
            pos = letters.index(letter)
            new_pos = pos + shift
            encrypted_text += letters[new_pos]
        else:
            encrypted_text += letter
    print(f"The {direction}c text text is: {encrypted_text}")


letters = list(string.ascii_lowercase + string.ascii_lowercase)
work = True

while exit:
    direction = input("Type (E)ncode to encrypt or (D)ecode to decrypt: ").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    ceaser(text, shift, direction)
    answer = input("exit? yes, no\n")
    if answer == "yes":
        exit = False
