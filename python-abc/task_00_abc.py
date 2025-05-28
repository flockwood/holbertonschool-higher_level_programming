#!/usr/bin/env python3

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class that defines the interface for animals."""

    @abstractmethod
    def sound(self):
        """Return the sound this animal makes."""
        pass


class Dog(Animal):
    """Concrete class representing a dog."""

    def sound(self):
        """Return the sound this dog makes."""
        return "Bark"


class Cat(Animal):
    """Concrete class representing a cat."""

    def sound(self):
        """Return the sound this cat makes."""
        return "Meow"
