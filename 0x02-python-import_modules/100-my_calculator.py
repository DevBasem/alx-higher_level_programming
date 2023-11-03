#!/usr/bin/python3

def main():
    import sys
    from calculator_1 import add, sub, mul, div
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a, operator, b = sys.argv[1], sys.argv[2], sys.argv[3]

    if operator not in ('+', '-', '*', '/'):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    try:
        a, b = int(a), int(b)
    except ValueError:
        print("Arguments should be integers.")
        sys.exit(1)

    if operator == '+':
        result = add(a, b)
    elif operator == '-':
        result = sub(a, b)
    elif operator == '*':
        result = mul(a, b)
    else:
        if b == 0:
            print("Error: Division by zero")
            sys.exit(1)
        result = div(a, b)

    print(f"{a} {operator} {b} = {result}")

if __name__ == "__main__":
    main()

