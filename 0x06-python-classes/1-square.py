#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Class that defines properties of square."""

    def __init__(self, size):
        """Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square.

        Note:
            The size attribute is private and is prefixed with
            a double underscore.
        """
        self.__size = size
