from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2
    return 0

operation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def New_calculator():
    print(logo)
    Continue = True
    n1 = float(input("What's the first number: "))
    while Continue:
        for symbols in operation:
            print(symbols)
        chosen_symbol = input("Pick an operation symbol from above: ")
        n2 = float(input("What's the next number: "))
        calculation_function = operation[chosen_symbol]
        answer = calculation_function(n1, n2)
        print(f"{n1} {chosen_symbol} {n2} = {answer}")
        user_input = input(f"Type y to continue with {answer} or type n to exit: ")
        if user_input == "y":
            n1 = answer
        else:
            Continue = False
            New_calculator()
New_calculator()
