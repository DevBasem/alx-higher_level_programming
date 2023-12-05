#!/usr/bin/python3
"""write_file module"""


def write_file(filename="", text=""):
    """
    write_file - writes a string to a text file (UTF8)
    and returns the number of characters written

    Args:
        filename (str): Name of the file to be written.
        text (str): The string to be written to the file.

    Returns:
        int: The number of characters written.
    """
    with open(filename, "w", encoding="UTF-8") as f:
        nb_characters = f.write(text)
    return nb_characters
