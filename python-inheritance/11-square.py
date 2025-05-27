#!/usr/bin/python3
"""
Module 11-square
Defines a Square class that inherits from Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class representing a square.
    """

    def __init__(self, size):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is not greater than 0.
        """
        self.integer_validator("size", size)  # Validate size
        self.__size = size  # make size private

        super().__init__(size, size)

    def area(self):
        """
        Returns the area of the square.

        Returns:
            int: The area of the square (size * size).
        """
        return self.__size * self.__size  # Area fx

    def __str__(self):
        """
        Returns a string representation of the square.

        Returns:
            str: The formatted string "[Square] <size>/<size>".
        """

        return f"[Square] {self.__size}/{self.__size}"
