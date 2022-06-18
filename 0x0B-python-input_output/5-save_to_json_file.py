#!/usr/bin/python3
"""
0x0B-python-input_output
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Save a Python object to a JSON file
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
