#!/usr/bin/python3


"""
This module defines a single function, from_json_string.

The function returns a Python data structure represented by a JSON string.
No exception handling is needed for invalid JSON strings.
"""
import json


def from_json_string(my_str):
    """
    Return a Python object represented by a JSOn string.

    Args:
        my_str (str): The JSON string to convert to Python object.

    Returns:
        object: Python data structure represented by the JSON string.
    """
    return json.loads(my_str)
