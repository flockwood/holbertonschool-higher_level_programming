#!/usr/bin/python3


"""
This module defines a single function, class_to_json.

The function returns the dictionary description with simple data structure
for JSOn serialization of an object. All attributes are assumed to be
serializable.
"""

def class_to_json(obj):
    """
    Return the dictionary description of an object for JSOn serialization.

    Args:
        obj: An instance of a Class with serializable attributes.

    Returns:
        dict: Dictionary containing all serializable attributes of the object.
    """
    return obj.__dict__
