#!/usr/bin/python3
"""This module defines a Square class with size and position validation."""


class Square:
    """Represents a square with size and position attributes."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square with a given size and position.

        Args:
            size (int): The size of the square (default is 0).
            position (tuple): The position of the square (default is (0, 0)).

        Raises:
            TypeError: If size or position are invalid.
            ValueError: If size is less than 0.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation.

        Args:
            value (int): The size to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square with validation.

        Args:
            value (tuple): The position to set.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if (
            not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(num, int) and num >= 0 for num in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square with the character # and respect position."""
        if self.__size == 0:
            print("")  # Print an empty line if size is 0
            return

        # Print empty lines for vertical offset (position[1])
        for _ in range(self.__position[1]):
            print("")

        # Print the square with spaces for horizontal offset (position[0])
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
