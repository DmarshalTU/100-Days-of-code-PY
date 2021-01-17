import random


def random_number():
    computer_guess = random.randint(0, 101)
    return computer_guess


def check_difficulty(user_choose):
    attempts = 5
    if user_choose == "h":
        return attempts
    else:
        attempts = 10
        return attempts


def game(attempts, user_guess):
    while user_guess != random_number and attempts > 0:
        if user_guess == random_number:
            print("You won!")
        elif user_guess > random_number:
            print(f"To high.\nYou have  {attempts} left.")
        else:
            print(f"To low.\nYou have  {attempts} left.")

        attempts -= 1
        user_guess = int(input("Make a guess: "))
    print("Game Over.")


if __name__ == '__main__':
    random_number = random_number()
    print(random_number)

    print("Welcome to the Number Guessing Game!")

    difficulty = input('choose a difficulty. Type (E)asy or (H)ard: ').lower()
    attempts = check_difficulty(difficulty)
    print(f"You have {attempts} to try.")

    user_guess = int(input("Make a guess: "))
    print(user_guess)

    game(attempts, user_guess)