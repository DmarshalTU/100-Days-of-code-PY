print("Welcome to the rollercoaster!")
height = int(input("What is your height? "))

if height >= 120:
    print("You can pass")
    age = int(input("What is yor age? "))
    if age < 12:
        print("Please pay 5$.")
    elif age < 18:
        print("Please pay 7$.")
    else:
        print("Please pay 12$.")
else:
    print("You cannot pass")

#number  =  int(input("What number do you want to check? "))
#if number % 2 == 0:
#    print(f"The number: {number} is even.")
#else:
#    print(f"The number: {number} is odd.")


