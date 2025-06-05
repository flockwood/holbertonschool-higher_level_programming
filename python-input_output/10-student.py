#!/usr/bin/python3
"""
Module: 10- student

Defines a Student class than can provide a custom dictionary
representation of itself based on a list of desired attributes.
"""


class Student:
    def __init__(self, first_name, last_name, age):
        """
        Initialize a new Student

        Args:
            first_name (str): Student's first name.
            last_name (str): Student's last name.
            age (int): Student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation of the Student.

        If attrs is a list of strings, only those attributes are included.
        Otherwise, all attributes are returned.

        Returns:
            dict: The dictionary representation of the Student.
        """
        if isinstance(attrs, list) and all(
                isinstance(attr, str) for attr in attrs):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__
