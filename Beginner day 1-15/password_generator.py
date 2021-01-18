import random
import string


print("Welcome to the PyPassword Generator!")

letters = int(input("How many letters? \n"))
symbols = int(input("How many symbols? \n"))
numbers = int(input("How many numbers? \n"))

alpha = string.ascii_lowercase + string.ascii_uppercase
numbers_0 = string.digits
symbols_0 = string.punctuation

password = ''

for letter in range(0, letters):
    password += random.choice(alpha)
for symbol in range(0, symbols): 
    password += random.choice(symbols_0)
for number in range(0, numbers):
    password += random.choice(numbers_0)
print(password)
shuffeld_pass = list(password)
random.shuffle(shuffeld_pass)
print(''.join(shuffeld_pass))
