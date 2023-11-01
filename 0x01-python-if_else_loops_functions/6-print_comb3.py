#!/usr/bin/python3
for first_digit in range(9):
    for second_digit in range(first_digit + 1, 10):
        if first_digit < 8:
            print("{:01d}{:01d}, ".format(first_digit, second_digit), end='')
        else:
            print("{:01d}{:01d}".format(first_digit, second_digit))
