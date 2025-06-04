#!/usr/bin/python3


"""
This module defines a single function, to_json_string.

The function returns the JSON representation of an object as a string.
No exception handling is needed for non-serializable objects.
"""
import json


def to_json_string(my_obj):
    """
    Return the JSOn representation of an object as a string.

    Args:
        my_obj: The object to convert to JSON string.

    Returns:
        str: JSON string representation of the object.
    """
    return json.dumps(my_obj)
