#!/usr/bin/python3
"""
Module: 12-pascal_triangle

Defines a function to generate Pascal's triangle.

The pascal_triangle(n) function returns a list of lists of integers
representing the first n rows of Pascal's triangle.
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing
    Pascal's triangle of n.

    Args:
        n (int): The number of rows to generate.

    Returns:
        list: Pascal's tringle as a list of lists.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for row_num in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]
        for i in range(1, len(prev_row)):
            new_row.append(prev_row[i - 1] + prev_row[i])
        new_row.append(1)
        triangle.append(new_row)
    return triangle
