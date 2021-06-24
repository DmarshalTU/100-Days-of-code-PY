print(f"Welcome to the Love Calcolator!")

name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_string = (name1 + name2).lower()
t = combined_string.count("t")
r = combined_string.count("r")
u = combined_string.count("u")
e = combined_string.count("e")
l = combined_string.count("l")
o = combined_string.count("o")
v = combined_string.count("v")
e = combined_string.count("e")

true = t + r + u + e
love = l + o + v + e
total = int(str(true) + str(love))

if total < 10 or total > 90:
    print(f"Your score is: {total}, you go together like coke and mentos.")
elif total > 40 and total < 50:
    print(f"Youre score: {total}, you alright together.")
else:
    print(f"Your score is: {total}.")
