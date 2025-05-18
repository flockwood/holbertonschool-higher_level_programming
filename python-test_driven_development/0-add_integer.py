#!/usr/bin/python3
"""Defines a addition function"""


def add_integer(a, b=98):
    """
    Adds to integers.

    Args:
        a (int or float): value to be added.
        b (int or float, optional): value to be added. Defaults to 98.

    Returns:
        int: the addition of a and b.

    Raises:
        TypeError: if either a or b is not an integer or a float.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
