import random

print("Welcome to Banker Rulette.")

people = input("Enter the names seperated with ',' :").split(",")
print(people)
#random_banker = people[random.randint(0, len(people) - 1)]
random_banker = random.choice(people)
print(f"The payer is {random_banker}")
