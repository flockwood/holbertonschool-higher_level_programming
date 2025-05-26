#!/usr/bin/python3
"""Define a function named lookup"""


def lookup(obj):
    """Returns the list of available attributes and
        methods of an object.

    Args:
        obj: An object

    Returns:
        List: object.
    """
    return dir(obj)
