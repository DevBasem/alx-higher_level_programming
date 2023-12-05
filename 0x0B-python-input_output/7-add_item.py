#!/usr/bin/python3
"""7-add_item module"""

import sys
import json
import os.path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"

# Load existing list from the file or create an empty list
my_list = load_from_json_file(filename)

# Add command-line arguments to the list
my_list.extend(sys.argv[1:])

# Save the updated list to the file
save_to_json_file(my_list, filename)
