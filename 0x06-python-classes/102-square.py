#!/usr/bin/python3
"""Square class definition"""


class Square:
    """Square class with size attribute"""

    def __init__(self, size=0):
        """Initialize square with size"""
        self.__size = size

    def area(self):
        """Calculate square area"""
        return self.__size ** 2

    @property
    def size(self):
        """Return square size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set square size, must be integer >= 0"""
        if not isinstance(value, int) or value < 0:
            raise ValueError("size must be an integer >= 0")
        self.__size = value

    def __lt__(self, other):
        """Check if square area is less than another"""
        return self.__size < other.__size

    def __le__(self, other):
        """Check if square area is less than or equal to another"""
        return self.__size <= other.__size

    def __eq__(self, other):
        """Check if square area is equal to another"""
        return self.__size == other.__size

    def __ne__(self, other):
        """Check if square area is not equal to another"""
        return self.__size != other.__size

    def __gt__(self, other):
        """Check if square area is greater than another"""
        return self.__size > other.__size

    def __ge__(self, other):
        """Check if square area is greater than or equal to another"""
        return self.__size >= other.__size
