#!/usr/bin/python3
"""
This module defines the is_same_class function.

Functions:
    is_same_class(obj, a_class): Returns True if obj is
    an instance of a_class, otherwise False.
"""


def is_same_class(obj, a_class):
    """
    Returns True if obj is an instance of a_class, otherwise False.

    Args:
        obj (object): The object to check.
        a_class (type): The class to compare against.

    Returns:
        bool: True if obj is an instance of a_class, False otherwise.
    """
    return type(obj) is a_class
