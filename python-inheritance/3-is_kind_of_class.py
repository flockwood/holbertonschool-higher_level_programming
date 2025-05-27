#!/usr/bin/python3
"""
Module 3-is_kind_of_class
Defines a function that checks if an object is an instance of a class
or a class that inherited from it.
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if obj is an instance of a_class or a subclass of it.

    Args:
        obj (any): The object to check.
        a_class (type): The class to compare.

    Returns:
        bool: True if obj is an instance of a_class or a subclass,
        otherwise False.
    """
    return isinstance(obj, a_class)
