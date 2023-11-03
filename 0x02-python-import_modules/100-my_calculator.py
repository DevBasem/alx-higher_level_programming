#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    operators = ["+", "-", "*", "/"]
    argv = sys.argv[1:]
    argc = len(argv)

    if argc != 3:
        print("Usage: {} <a> <operator> <b>".format(sys.argv[0]))
        sys.exit(1)

    operator = argv[1]

    if operator not in operators:
        print("Unknown operator. Available operators: +, -, *, and /")
        sys.exit(1)

    a, b = int(argv[0]), int(argv[2])

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
        result = div(a, b)
        print("{:d} / {:d} = {:d}".format(a, b, result))

