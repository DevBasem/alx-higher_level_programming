#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """
    Class that defines a square.

    Attributes:
        size (int): Size of the square.
        position (tuple): Position of the square.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): Size of the square (default is 0).
            position (tuple): Position of the square (default is (0, 0)).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            int: Size of the square.
        """
        return self._size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): New size for the square.

        Raises:
            TypeError: If the provided value is not an integer.
            ValueError: If the provided value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    @property
    def position(self):
        """
        Retrieves the position of the square.

        Returns:
            tuple: Position of the square.
        """
        return self._position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square.

        Args:
            value (tuple): New position for the square.

        Raises:
            TypeError: If the provided value is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self._position = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: Area of the square.
        """
        return self.size ** 2

    def my_print(self):
        """
        Prints the square using the character #.

        If size is equal to 0, prints an empty line.
        Position is used by adding spaces.

        Printing a Square instance should have the same behavior as my_print().
        """
        if self.size == 0:
            print()
            return

        for _ in range(self.position[1]):
            print()

        for _ in range(self.size):
            print(" " * self.position[0] + "#" * self.size)
