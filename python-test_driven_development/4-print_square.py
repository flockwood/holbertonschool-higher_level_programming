#!/usr/bin/python3
"""Defines a function to print a square"""


def print_square(size):
    """Function that prints a square with the character #.

    Args:
        size (int): the size length of the square.

    Raises:
        TypeError: if size is not an integer or
                    if size is a float an less than 0.
        ValueError: if size is less than 0.
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        print("#" * size)
