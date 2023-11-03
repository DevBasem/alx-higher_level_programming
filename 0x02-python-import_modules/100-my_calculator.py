#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

def main():
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = sys.argv[1]
    operator = sys.argv[2]
    b = sys.argv[3]

    if operator not in ('+', '-', '*', '/'):
        print("Unknown operator. Available operators: +, -, *, and /")
        sys.exit(1)
    else:
        a, b = int(a), int(b)
        if operator == '+':
            result = add(a, b)
        elif operator == '-':
            result = sub(a, b)
        elif operator == '*':
            result = mul(a, b)
        elif operator == '/':
            if b == 0:
                print("Error: Division by zero")
                sys.exit(1)
            result = div(a, b)

    output = "{} {} {} = {}".format(a, operator, b, result)
    print(output)

if __name__ == "__main__":
    main()
