#!/usr/bin/python3
"""add_item module"""

import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file


def add_items_to_json_list(file_path):
    """
    Adds command-line arguments to a Python list and saves them to a JSON file.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        None
    """
    json_list = []

    if os.path.exists(file_path):
        json_list = load_from_json_file(file_path)

    for arg in sys.argv[1:]:
        json_list.append(arg)

    save_to_json_file(json_list, file_path)
