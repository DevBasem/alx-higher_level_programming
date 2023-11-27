#!/usr/bin/python3
"""Rectangle class for Holberton Python project 0x08 task 2.
"""


class Rectangle:
    """Defines a rectangle with width and height attributes.

    Attributes:
        __width (int): Horizontal dimension.
        __height (int): Vertical dimension.

    """
    def __init__(self, width=0, height=0):
        """Initializes a Rectangle instance.

        Args:
            width (int): Horizontal dimension, defaults to 0.
            height (int): Vertical dimension, defaults to 0.

        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for the width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the width attribute."""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Getter for the height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the height attribute."""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates and returns the perimeter of the rectangle."""
        return (self.__width + self.__height) * 2
