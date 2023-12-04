#!/usr/bin/python3
"""
This module defines the MyList class, a subclass of list.

Classes:
    MyList: Inherits from list and adds a print_sorted method.
"""


class MyList(list):
    """
    A subclass of list with an additional method for printing
    the list in sorted order.
    """

    def print_sorted(self):
        """
        Prints the list in ascending order.

        Returns:
            None
        """
        print(sorted(self))
