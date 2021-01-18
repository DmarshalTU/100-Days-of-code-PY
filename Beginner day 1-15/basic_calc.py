def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mul(n1, n2):
    return n1 * n2


def dev(n1, n2):
    return "{:.2f}".format(n1 / n2)


operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": dev,
}


def calc():
    num1 = float(input("Enter the firs number: "))

    for symbol in operations:
        print(symbol)

    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")

        num2 = float(input("Enter the next number: "))

        calc_func = operations[operation_symbol]
        answer = calc_func(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type y to continue with {answer} or n to start new calculation: ").lower() == "y":
            num1 = answer
        else:
            should_continue = False
            calc()


calc()
