#!/usr/bin/python3
"""add_item module"""

from sys import argv
from importlib import import_module

load_file = import_module('6-load_from_json_file').load_from_json_file
save_file = import_module('5-save_to_json_file').save_to_json_file

try:
    json_list = load_file('add_item.json')
except (ValueError, FileNotFoundError):
    json_list = []

for item in argv[1:]:
    json_list.append(item)

save_file(json_list, 'add_item.json')
