#!/usr/bin/python3

import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    operators = {"+": add, "-": sub, "*": mul, "/": div}
    
    if len(sys.argv) != 4:
        print("Usage: ./calculator.py <a> <operator> <b>")
        sys.exit(1)
    
    a, operator, b = map(str, sys.argv[1:])
    
    if operator not in operators:
        print("Unknown operator. Available operators: +, -, *, and /")
        sys.exit(1)
    
    try:
        a, b = float(a), float(b)
        result = operators[operator](a, b)
        print("{:.1f} {} {:.1f} = {:.1f}".format(a, operator, b, result))
    except ValueError:
        print("Error: Please enter valid numeric inputs for 'a' and 'b'")
        sys.exit(1)
