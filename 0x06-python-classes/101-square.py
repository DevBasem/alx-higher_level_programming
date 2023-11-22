#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """
    Class that defines properties of square.

    Attributes:
        side_length: length of a square side.
    """

    def __init__(self, side_length=0, location=(0, 0)):
        """Creates new instances of square.

        Args:
            side_length (int): length of the square side.
            location (tuple): location of the square.
        """
        self.side_length = side_length
        self.location = location

    def area(self):
        """Calculates the area of square.

        Returns: the current square area.
        """
        return self.side_length ** 2

    @property
    def side_length(self):
        """Returns the length of a square side
        """
        return self.__side_length

    @side_length.setter
    def side_length(self, value):
        """Property setter for side_length.

        Args:
            value (int): length of a square side.

        Raises:
            TypeError: side_length must be an integer.
            ValueError: side_length must be >= 0.
        """
        if not isinstance(value, int):
            raise TypeError("side_length must be an integer")
        if value < 0:
            raise ValueError("side_length must be >= 0")
        self.__side_length = value

    @property
    def location(self):
        """Returns the location of the square
        """
        return self.__location

    @location.setter
    def location(self, value):
        """Property setter for location.

        Args:
            value (tuple): location of the square.

        Raises:
            TypeError: location must be a tuple of 2 positive integers
        """
        if not isinstance(value, tuple):
            raise TypeError("location must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("location must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("location must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("location must be a tuple of 2 positive integers")
        self.__location = value

    def print_square(self):
        """prints in stdout the square with the character #
        """

        if self.__side_length == 0:
            print()
        else:
            for j in range(self.__location[1]):
                print()
            for i in range(self.__side_length):
                for k in range(self.__location[0]):
                    print(" ", end="")
                print("#" * (self.__side_length))

    def __str__(self):
        """Prints square offsetting it by location with symbol #

        Returns: The square.
        """
        if self.__side_length == 0:
            return ''
        new_lines = '\n' * self.location[1]
        spaces = ' ' * self.location[0]
        hashes = '#' * self.side_length
        return new_lines + '\n'.join([spaces + hashes] * self.side_length)
