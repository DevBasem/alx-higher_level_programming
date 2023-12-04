#!/usr/bin/python3
"""
This module defines the BaseGeometry class.

Classes:
    BaseGeometry: An empty class with an area method.
"""


class BaseGeometry:
    """
    An empty class with an area method.
    """

    def area(self):
        """
        Raises an Exception with the message 'area()
        is not implemented.'

        Raises:
            Exception: Always raises an Exception.
        """
        raise Exception("area() is not implemented")
