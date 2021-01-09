print("Welcome to Python Pizza Deliveries!")

size = input("What size pizza do you want? (S)mall, (M)edium, (L)arge? >>> ")
add_pepperoni = input("Do you want pepperoni? (Y)es, (N)o? >>> ")
extra_cheese =input("Do you want extra cheese? (Y)es, (N)o? >>> ")

# Pizza size
small_pizza = 15
medium_pizza = 20
large_pizza = 25

# Additional
pepperoni = 2
pepperoni_m_l = 3
chesse = 1

price = 0

if size == "S":
    price += small_pizza
elif size == "M":
    price += medium_pizza
else:
    price += large_pizza

if add_pepperoni == "Y" and size == "S":
    price += pepperoni
else:
    price += pepperoni_m_l

if extra_cheese == "Y":
    price += chesse

print(f"Your price is: ${price}.")
