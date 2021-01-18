import random

random_integer = random.randint(1, 10)
print(random_integer)

random_side = random.randint(0, 1)
if random_side == 1:
    print("Heads")
else:
    print("Tails")
