#!/usr/bin/python3
"""
Square Class Module

This module defines the Square class, a subclass of Rectangle.
"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    Square class

    Attributes:
        __size (int): Private attribute representing
        the size of the square.

    Methods:
        __init__(self, size): Initializes a Square
        instance with a given size.
        area(self): Computes the area of the square.
        __str__(self): Returns a string representation of the square.
    """

    def __init__(self, size):
        """
        Initializes a square with a given size.

        Args:
            size (int): The size of the square.
        """
        # Updated variable naming for clarity
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Computes the area of the square.

        Returns:
            int: The area of the square.
        """
        # Updated variable naming for clarity
        return self.__size ** 2

    def __str__(self):
        """
        Returns a string representation of the square.

        Returns:
            str: A string representation of the square.
        """
        # Updated variable naming for clarity
        return "[Square] {}/{}".format(self.__size, self.__size)
