#!/usr/bin/python3
"""
This module defines the MyInt class.
"""


class MyInt(int):
    """
    MyInt class, inheriting from int with inverted == and != operators.
    """

    def __eq__(self, other):
        """
        Inverts the behavior of the == operator.

        Args:
            other: The other object to compare.

        Returns:
            bool: True if not equal, False if equal.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Inverts the behavior of the != operator.

        Args:
            other: The other object to compare.

        Returns:
            bool: True if equal, False if not equal.
        """
        return super().__eq__(other)
