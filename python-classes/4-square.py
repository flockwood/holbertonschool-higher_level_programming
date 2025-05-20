#!/usr/bin/python3
"""This module defines a square class with size validation"""


class Square:
    """Represents a square woth a private size attribute."""

    def __init__(self, size=0):
        """Initialize a new square with a given size
        Args:
            size (int): The size of the square (default is 0).
        
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less tham 0.
        """
        self.size = size  # Calls the setter method for validation

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation
        Args:
            value (int): The size to set.
            
        Raises:
            TypeError: If valie is not an integer.
            ValueError: If value is less than 0.
        """

        if  not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise TypeError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return tha area of the square."""
        return self.__size * self.__size
