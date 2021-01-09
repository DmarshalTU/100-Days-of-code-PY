height = int(input("What is your heght? "))

if height >= 120:
    print("Can ride!")
    age = int(input("What is yor age? "))
    price = 0
    if age < 12:
        price = 5
        print(f"Your price ${price}")
    elif age < 18:
        price = 7
        print(f"Your price ${price}")
    else:
        price = 12
    photo = input("Do you want photo? ")
    if photo == "yes":
        price += 3
    print(f"The total price is: ${price}")
else:
    print("Cant ride!")
