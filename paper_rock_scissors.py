import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

print(rock, paper, scissors)
print("Welcome to Rock, Paper, Scissors.")
player = input("What do you choose? (R)ock, (P)aper or (S)cissors? ").lower()

options = [rock, paper, scissors]

computer_random = random.randint(0, len(options) -1)

print("You picked: ")
if player == "r":
    print(options[0])
elif player == "p":
    print(options[1])
else:
    print(options[2])

print("Computer picked: ")
print(options[computer_random])

if player == "r" and not computer_random == 0:
    if computer_random == 2:
        print("You win!")
    else:
        print("You lose!")
elif player == "p" and not computer_random == 1:
    if computer_random == 0:
        print("You win!")
    else:
        print("You lose!")
elif player == "s" and not computer_random == 2:
    if computer_random == 1:
        print("You win!")
    else:
        print("You lose!")
else:
    print("Its a tay.")
