#!/usr/bin/python3
"""
This module defines the add_integer function.

This function adds two integers.
a and b must be integers or floats; otherwise, it raises a TypeError
exception with the message 'a must be an integer' or 'b must be an integer.'
a and b are first casted to integers if they are floats.

Returns:
    An integer: the addition of a and b
"""


def add_integer(a, b=98):
    """
    Adds two integers.

    Arguments:
        a (int or float): The first integer.
        b (int or float): The second integer. Default is 98.

    Returns:
        int: The addition of a and b.
    """
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, int):
        raise TypeError("b must be an integer")
    return a + b
