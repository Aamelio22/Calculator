from art import logo

calc = "run"
dir = "n"
result = 0

print(logo)


# Add
def add(n1, n2):
    return n1 + n2


# Subtract
def subtract(n1, n2):
    return n1 - n2


# Multiply
def multiply(n1, n2):
    return n1 * n2


# Divide
def divide(n1, n2):
    return n1 / n2


operators = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


# Get first number
def get_n1():
    while True:
        n1 = int(input("What is the first number?: "))
        if str(n1).isdigit() == False:
            print("Error, please enter only numbers.\n")
        else:
            return n1
            break


# Get operator
def get_op():
    while True:
        for op in operators:
            print(op)
        operator = input("What operation would you like to perform?: ")
        if operator not in operators:
            print("Error, invalid input.\n")
        else:
            return operator
            break

        # Get second number


def get_n2():
    while True:
        n2 = int(input("What is the second number?: "))
        if str(n2).isdigit() == False:
            print("Error, please enter only numbers.\n")
        else:
            return n2
            break


# Get result of calculation
def get_result(n1, operator, n2, ):
    operators = {"+": add(n1, n2), "-": subtract(n1, n2), "*": multiply(n1, n2), "/": divide(n1, n2)}
    result = float(operators[operator])
    if operator == "+":
        print(f'{n1} + {n2} = {result}')
    elif operator == "-":
        print(f'{n1} - {n2} = {result}')
    elif operator == "*":
        print(f'{n1} * {n2} = {result}')
    else:
        print(f'{n1} / {n2} = {result}')
    return result


# Run again or continue calculation
def get_dir():
    while True:
        dir = input(
            f"Type 'c' to continue calculating with {result}, type 'n' to start a new calculation, or type 'q' to quit: ")
        if dir == "c" or "n" or "q":
            return dir
            break
        else:
            print("Error, invalid input.\n")

        # Equation


while calc == "run":
    if dir == "n":
        n1 = get_n1()
    else:
        n1 = result
    operator = get_op()
    n2 = get_n2()
    result = get_result(n1, operator, n2)
    dir = get_dir()
    if dir == "q":
        calc = "quit"