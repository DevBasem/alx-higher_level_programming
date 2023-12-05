#!/usr/bin/python3
"""stats module"""

import sys


def print_stats(total_size, status_codes):
    """
    Prints statistics based on total file size
    and number of lines by status code.

    Args:
        total_size (int): Total file size.
        status_codes (dict): Dictionary containing counts of
        lines for each status code.
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))
