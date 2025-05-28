#!/usr/bin/env python3

from abc import ABC, abstractmethod

class Animal(ABC):

    """
    Abstract class that defines the base structure for the animal.
    Obligates all subclasses to implement the sound() method.
    """
    @abstractmethod
    def sound(self):
        """Abstract method that every sublass must include."""
        pass

class Dog(Animal):
    """
    Class that represents a dog. Implements the sound() method.
    """
    def sound(self):
        return "Bark"

class Cat(Animal):
    """
    Class that represents a cat. Implements the sound() method.
    """
