#!/usr/bin/python3
"""Deines a rectangle class with width and height validation."""

class Rectangle:
    """Represents a rectangle."""
    def __init__(self, width=0, height=0):
        """Initialize a new rectangle.
        
        Args:
            width (int): The width of the rectangle (default is 0).
            height (int): The height of the rectangle (default is 0).
            
        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than 0.
            """
            
            self.width = width
            self.height = height

        @property
        def width(self):
            """Retrieve the width of the rectangle."""
            return self.__width

        @width.setter
        def width(self, value):
            """Set the width of the rectangle with validation.
            
            Args:
                value (int): The width to set.
                
            Raises:
                TypeError: If value is not an integer.
                ValueError: If value is less than 0.
            """
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("witdh must be >= 0")
            self.__width = value

        @property
        def height(self):
            """Retrieve the height of the rectangle."""
            return self.__height

        @height.setter
        def height(self, value):
            """Set the height of the rectangle with validation.
            
            Args:
                value (int): The height to set.

            Raises:
                TypeError: If value is mnot na integer.
                ValueError: If value os less than 0.
            """
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value
