#!/usr/bin/python3

import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    argv = sys.argv[1:]
    argv_count = len(argv)
    operators = ["+", "-", "*", "/"]
    
    if argv_count != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif sys.argv[2] not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        if sys.argv[2] == "+":
            result = add(a, b)
            print("{:d} + {:d} = {:d}".format(a, b, result))
        elif sys.argv[2] == "-":
            result = sub(a, b)
            print("{:d} - {:d} = {:d}".format(a, b, result))
        elif sys.argv[2] == "*":
            result = mul(a, b)
            print("{:d} * {:d} = {:d}".format(a, b, result))
        elif sys.argv[2] == "/":
            result = div(a, b)
            print("{:d} / {:d} = {:d}".format(a, b, result))
