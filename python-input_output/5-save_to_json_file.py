#!/usr/bin/python3

"""
This module defines a single function, save_to_json_file

The function writes an object to a text file using JSON representation.
No exception handling is needed for serialization or file permissions.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Write an object to a text file using JSON representation.

    Args:
        my_obj: The object to serialize and save to file.
        filename (str): The name of the file to write to.
    """
    with open(filename, 'w', enconding='utf-8') as file:
        json.dump(my_obj, file)
