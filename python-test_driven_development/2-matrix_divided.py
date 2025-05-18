#!/usr/bin/python3
"""Defines a matrix division function"""


def matrix_divided(matrix, div):
    """Divides all the elements of a matrix.

    Args:
        matrix (int or float): Is a list of lists of integers or floats.
        div (int or float): Must be a number, can't be equal to 0.

    Returns:
        A new matrix.

    Raises:
        TypeError: if matrix is not a list of lists of integers of floats.
        TypeError: if div isn't a number.
        ZeroDivisionError: if div is 0
    """

    if (not isinstance(matrix, list) or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

        if not all(isinstance(element, (int, float)) for element in row):
            raise TypeError("matrix must be a matrix (list of lists) of "
                            "integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(element / div, 2) for element in row] for row in matrix]
