#!/usr/bin/python3
"""Module magic_string
Returns a string "Holberton" repeated n times.
"""


def magic_string():
    """Returns a string "Holberton" repeated n times."""
    magic_string.c = getattr(magic_string, "c", 0) + 1
    return (("Holberton, " * magic_string.c)[:-2])
