#!/usr/bin/python3

import sys
from calculator_1 import add, sub, mul, div

def main():
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a, operator, b = sys.argv[1], sys.argv[2], sys.argv[3]

    if operator not in ["+", "-", "*", "/"]:
        print("Unknown operator. Available operators: +, -, *, and /")
        sys.exit(1)

    try:
        a, b = int(a), int(b)

        if operator == "+":
            result = add(a, b)
            print("{:d} + {:d} = {:d}".format(a, b, result))
        elif operator == "-":
            result = sub(a, b)
            print("{:d} - {:d} = {:d}".format(a, b, result))
        elif operator == "*":
            result = mul(a, b)
            print("{:d} * {:d} = {:d}".format(a, b, result))
        elif operator == "/":
            if b == 0:
                print("Error: Division by zero is not allowed")
                sys.exit(1)
            result = div(a, b)
            print("{:d} / {:d} = {:d}".format(a, b, result))
    except ValueError:
        print("Error: Please enter valid integer inputs for 'a' and 'b")
        sys.exit(1)

if __name__ == "__main__":
    main()
