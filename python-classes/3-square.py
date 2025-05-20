#!/usr/bin/python3
"""This module defines a Square Class"""

class Square:
    """Represents a square with a private size attribute"""

    def __init__(self, size=0):
        """Initialize a new Square with a given size
        
        Args:
           size (int): The size of the square (default is 0).
           
        Raises:
            TypeError: If the size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0: raise ValueError("size must be >= 0")
        self.__size = size 

    def area(self):
        """Returns the current square area."""
        return self.__size * self.__size
