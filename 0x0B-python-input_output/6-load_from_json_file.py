#!/usr/bin/python3
"""load_from_json_file module"""

import json


def load_from_json_file(filename):
    """
    load_from_json_file - creates an object from a JSON file

    Args:
        filename (str): The name of the JSON file to be loaded.

    Returns:
        object: The Python data structure loaded from the JSON file.
    """
    with open(filename, "r", encoding="UTF-8") as f:
        return json.load(f)
