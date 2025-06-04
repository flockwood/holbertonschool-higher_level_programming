#!/usr/bin/python3
"""
This module defines a single function, load_from_json_file.

The function creates an object from a JSON file.
No exception handling is needed for file or JSOn errors.
"""
import json


def load_from_json_file(filename):
    """
    Create an object from a JSON file.

    Args:
        filename (str): The name of the JSON file to load.

    Returns:
        object: Python data structure loaded from the JSON file.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
