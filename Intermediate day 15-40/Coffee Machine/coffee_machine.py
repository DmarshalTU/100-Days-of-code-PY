from menu import MENU, resources

is_on = True
money = 0


def is_resource_sufficient(order_ingredients):
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            is_enough = False
    return is_enough


def process_coins():
    print("Please insert coins.")
    total = int(input("how many quarters?:")) * 0.25
    total += int(input("how many dimes?:")) * 0.1
    total += int(input("how many nickles?:")) * 0.05
    total += int(input("how many pennies?:")) * 0.01
    return total


def is_transaction_successful(money_recived, drink_cost):
    if money_recived >= drink_cost:
        change = round(money_recived - drink_cost, 2)
        print(f"Change amount: {change}")
        global money
        money += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}!☕☕☕")
    pass


# TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
while is_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    # TODO 2. Turn off the Coffee Machine by entering “off” to the prompt.
    if user_choice == "off":
        is_on = False
    elif user_choice == "report":
        # TODO 3. Print report.
        report = f"Water: {resources['water']}ml\n" \
                 f"Milk: {resources['milk']}ml\n" \
                 f"Coffee: {resources['coffee']}g\n" \
                 f"Money: ${money}"
        print(report)
    # TODO 4. Check resources sufficient?
    else:
        drink = MENU[user_choice]
        if is_resource_sufficient(drink["ingredients"]):
            # TODO 5. Process coins.
            payment = process_coins()
            # TODO 6. Check transaction successful?
            if is_transaction_successful(payment, drink["cost"]):
                # TODO 7. Make Coffee.
                make_coffee(user_choice, drink["ingredients"])
