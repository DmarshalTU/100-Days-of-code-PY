from game_data import data
import random


def format_data(account):
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]

    return f"{account_name}, a {account_description}, from {account_country}"


def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


print("Welcome to Highr Lower Game.")
score = 0
account_b = random.choice(data)

while score >= 0:
    account_a = account_b
    account_b = random.choice(data)

    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}\nVS\nCompare B: {format_data(account_b)}")

    guess = input("Who has more followers? type 'A' or 'B':\n").lower()

    a_folowwer_count = account_a["follower_count"]
    b_folowwer_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_folowwer_count, b_folowwer_count)

    if is_correct:
        score += 1
        print(f"You right! Current score: {score}")
    else:
        print(f"Sorry, you wrong! Final score: {score}")
        score = -1
