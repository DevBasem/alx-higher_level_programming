#!/usr/bin/python3
"""save_to_json_file module"""

import json


def save_to_json_file(my_obj, filename):
    """
    save_to_json_file - writes an object to a text file
    using a JSON representation

    Args:
        my_obj: The object to be serialized to JSON
        and written to the file.
        filename (str): The name of the file to be written.

    Returns:
        None
    """
    with open(filename, "w", encoding="UTF-8") as f:
        json.dump(my_obj, f)
