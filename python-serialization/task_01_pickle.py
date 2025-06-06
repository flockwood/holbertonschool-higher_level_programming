#!/usr/bin/env python3
"""
Custom object serialization module using pickle.

This module provides a CustomObject class that can serialize and deserialize
itself using the pickle module.
"""
import pickle


class CustomObject:
    """
    A custom Python class that demonstrates object serialization with pickle.
    
    Attributes:
        name (str): The name of the object
        age (int): The age value
        is_student (bool): Whether the object represents a student
    """
    
    def __init__(self, name, age, is_student):
        """
        Initialize a CustomObject instance.
        
        Args:
            name (str): The name of the object
            age (int): The age value
            is_student (bool): Whether the object represents a student
        """
        self.name = name
        self.age = age
        self.is_student = is_student
    
    def display(self):
        """
        Display the object's attributes in a formatted manner.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")
    
    def serialize(self, filename):
        """
        Serialize the current instance of the object and save it to a file.
        
        Args:
            filename (str): The filename to save the pickled object to
            
        Returns:
            None if an error occurs during serialization
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception:
            return None
    
    @classmethod
    def deserialize(cls, filename):
        """
        Load and return an instance of CustomObject from a pickled file.
        
        Args:
            filename (str): The filename to load the pickled object from
            
        Returns:
            CustomObject: The deserialized object instance, or None if error occurs
        """
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except (FileNotFoundError, pickle.PickleError, EOFError, Exception):
            return None
