#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    operators = ["+", "-", "*", "/"]

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a, operator, b = sys.argv[1], sys.argv[2], sys.argv[3]

    if operator not in operators:
        print("Unknown operator. Available operators: +, -, *, and /")
        sys.exit(1)

    try:
        a, b = int(a), int(b)
        result = None

        if operator == "+":
            result = add(a, b)
        elif operator == "-":
            result = sub(a, b)
        elif operator == "*":
            result = mul(a, b)
        elif operator == "/":
            result = div(a, b)

        if result is not None:
            print("{:d} {} {:d} = {:d}".format(a, operator, b, result))
    except ValueError:
        print("Error: Please enter valid integer inputs for 'a' and 'b")
        sys.exit(1)
