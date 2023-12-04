#!/usr/bin/python3
"""
This module defines the BaseGeometry class.

Classes:
    BaseGeometry: A class with area and integer_validator methods.
"""


class BaseGeometry:
    """
    A class with area and integer_validator methods.
    """

    def area(self):
        """
        Raises an Exception with the message 'area() is not implemented.'

        Raises:
            Exception: Always raises an Exception.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value.

        Args:
            name (str): The name of the value.
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
