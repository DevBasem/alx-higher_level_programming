#!/usr/bin/python3
"""
This module defines the inherits_from function.

Functions:
    inherits_from(obj, a_class): Returns True if obj is
    an instance of a class that inherited from a_class
    , otherwise False.
"""


def inherits_from(obj, a_class):
    """
    Returns True if obj is an instance of a class that
    inherited from a_class, otherwise False.

    Args:
        obj (object): The object to check.
        a_class (type): The class to compare against.

    Returns:
        bool: True if obj is an instance of a subclass of a_class
        , False otherwise.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
