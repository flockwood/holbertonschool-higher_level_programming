#!/usr/bin/env python3
 
"""
Module: Shape Duck Typing

This module demonstrates the use of abstract base classes and duck typing
in Python. The Shape abc provides a blueprint for Circle and Rectangle
classes, enforcing the area and perimeter methods. The shape_info function
demonstrates duck typing by calling methods without explicit type checking.

Classes:
    Shape:Abstract base class for geometric shapes.
    Circle: Implements area and perimeter for circles.
    Rectangle: Implements are and perimeter for rectangles.

User Example:
    circle = Circle(radius=5)
    rectangle = Rectangle(width=4, height)

    shape_info(circle)
    shape_info(rectangle)
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for shapes."""

    @abstractmethod
    def area(self):
        """Calculate and return the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate and return the perimeter of the shape."""
        pass


class Circle(Shape):
    """Implementation of a Circle."""
    def __init__(self, radius):
        """Initialize the circle with a radius."""
        self.radius = radius

    def area(self):
        """Calculate the area of the circle."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Calculate the perimeter of the circle."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Implementation of a Rectangle."""

    def __init__(self, width, height):
        """Initialize the rectangle with width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Calculate the are of the rectangle."""
        return self.width * self.height
    
    def perimeter(self):
        """Calculate the perimeter of the rectangle."""
        return 2 * (self.width + self.height)

def shape_info(shape):
    """Print the area and perimeter of a given shape, using duck typing."""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")

# Example
if __name__ == "__main__":
    circle = Circle(radius=5)
    rectangle = Rectangle(width=4, height=7)

    shape_info(circle)
    shape_info(rectangle)
