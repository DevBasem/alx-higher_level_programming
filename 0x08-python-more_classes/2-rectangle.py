#!/usr/bin/python3
"""2-rectangle."""


class Rectangle:
    """Defines a rectangle with width and height attributes.

    Attributes:
        _width (int): Horizontal dimension.
        _height (int): Vertical dimension.

    """
    def __init__(self, width=0, height=0):
        """Initializes a Rectangle instance.

        Args:
            width (int): Horizontal dimension (default 0).
            height (int): Vertical dimension (default 0).

        """
        self._width = width
        self._height = height

    @property
    def width(self):
        """Getter for the width attribute."""
        return self._width

    @width.setter
    def width(self, value):
        """Setter for the width attribute.

        Raises:
            TypeError: If value is not an int.
            ValueError: If value is less than 0.

        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self._width = value

    @property
    def height(self):
        """Getter for the height attribute."""
        return self._height

    @height.setter
    def height(self, value):
        """Setter for the height attribute.

        Raises:
            TypeError: If value is not an int.
            ValueError: If value is less than 0.

        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self._height = value

    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self._width * self._height

    def perimeter(self):
        """Calculates and returns the perimeter of the rectangle.

        Returns:
            0 if width or height is 0, otherwise returns the perimeter.

        """
        if self._width == 0 or self._height == 0:
            return 0
        else:
            return 2 * (self._width + self._height)
