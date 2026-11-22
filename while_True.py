def main():
    while True:
        x = int(input("X?: "))
        y = int(input("Y?: "))
        result = calculator(x, y)
        print(result)

        again = input("Continue? (y/n): ")
        if again == "n":
            break


def calculator(x, y):
    op = input("Operation (+, -, *, /): ")
    if op == "+":
        return x + y
    elif op == "-":
        return x - y
    elif op == "*":
        return x * y
    elif op == "/":
        if y == 0:
            return "Cannot divide by zero"
        return x / y
    else:
        return "Invalid operation"


main()