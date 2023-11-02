#!/usr/bin/python3

if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    result1 = add(a, b)
    result2 = sub(a, b)
    result3 = mul(a, b)
    result4 = div(a, b)
    print ('{} + {} = {}'.format(a, b, add(a, b)))
    print ('{} - {} = {}'.format(a, b, sub(a, b)))
    print ('{} * {} = {}'.format(a, b, mul(a, b)))
    print ('{} / {} = {}'.format(a, b, div(a, b)))
