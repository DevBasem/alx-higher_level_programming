#!/usr/bin/python3

def read_file(filename=""):
    """
    Reads a text file (UTF-8) and prints its content to stdout.

    Args:
        filename (str): The name of the file to be read.

    Returns:
        None
    """
    try:
        with open(filename, encoding='utf-8') as file:
            print(file.read(), end='')
    except Exception:
        pass
