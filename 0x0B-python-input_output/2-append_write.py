#!/usr/bin/python3
"""append_write module"""


def append_write(filename="", text=""):
    """
    append_write - appends a string at the end of a text file (UTF8) and returns the number of characters added

    Args:
        filename (str): Name of the file to be appended.
        text (str): The string to be appended to the file.

    Returns:
        int: The number of characters added.
    """
    with open(filename, "a", encoding="UTF-8") as f:
        nb_characters_added = f.write(text)
    return nb_characters_added
