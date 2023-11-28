#!/usr/bin/python3
"""
Module text_indentation
Prints a text with 2 new lines after each '.', '?', and ':'
"""


def text_indentation(text):
    """Prints text with added two newlines
    after each of these characters {'.', '?', ':'}.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    for delim in ".:?":
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])

    print("{}".format(text), end="")
