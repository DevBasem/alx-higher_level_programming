#!/usr/bin/python3
"""
This module defines the add_attribute function.
"""


def add_attribute(obj, attribute, value):
    """
    Adds a new attribute to an object if it's possible.

    Raises:
        TypeError: If the object can't have a new attribute.

    Args:
        obj: The object to which the attribute will be added.
        attribute: The name of the new attribute.
        value: The value to assign to the new attribute.
    """
    # Check if the object has __dict__ attribute
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")

    # Add the new attribute to the object
    setattr(obj, attribute, value)
