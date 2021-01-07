# Ex 1.1
print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")

# Ex 1.2
print("Day 1 - String Manipulation")
print("String Concatenation is done with the \"+\" s ign.")
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")

# Ex 1.3
# print("Hello " + input("What is your name? ") + "!")
print(len(input("What is your name? ")))

# Ex 1.4

# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

a, b = b, a


#Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)

# Final task

#1. Create a greeting for your program.
print("Welcome to the Band Name Generator!")
#2. Ask the user for the city that they grew up in.
city = input("What is the city that you grew up in? \n")
#3. Ask the user for the name of a pet.
pet_name = input("What is your pet name? \n")
#4. Combine the name of their city and pet and show them their band name.
print("The band name can be: " + city + " " + pet_name)
#5. Make sure the input cursor shows on a new line.
