#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args_number = len(sys.argv) - 1
    if args_number != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    calc = sys.argv[2]
    if calc != '+' and calc != '-' and calc != '*' and calc != '/':
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    from calculator_1 import add, sub, mul, div
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    if calc == '+':
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif calc == '-':
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif calc == '*':
        print("{} * {} = {}".format(a, b, mul(a, b)))
    else:
        print("{} / {} = {}".format(a, b, div(a, b)))
