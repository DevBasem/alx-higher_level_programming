#!/usr/bin/python3
"""
This module defines the is_kind_of_class function.

Functions:
    is_kind_of_class(obj, a_class): Returns True if obj is
    an instance of a_class or a subclass, otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if obj is an instance of a_class or a subclass
    , otherwise False.

    Args:
        obj (object): The object to check.
        a_class (type): The class to compare against.

    Returns:
        bool: True if obj is an instance of a_class or a subclass
        , False otherwise.
    """
    return isinstance(obj, a_class)
