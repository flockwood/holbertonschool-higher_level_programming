#!/usr/bin/python3
"""
Module 4-inherits_from
Defines a function that checks if an object is an instance of a class
that inherited (directly or indirectly) from the specified class.
"""


def inherits_from(obj, a_class):
    """
    Checks if obj is an instance of a subclass of a_class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to compare.

    Returns:
        bool: True if obj is an instance of a subclass of a_class,
              False if obj is exactly an instance of a_class or not related.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
