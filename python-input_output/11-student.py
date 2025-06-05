#!/usr/bin/python3
"""
Module: 11-student

Defines a Student class with serialization and deserialization.
"""


class Student:
    def __init__(self, first_name, last_name, age):
        """
        Initialize a new Student.

        Args:
            first_name (str): The student's first name.
            last_name (str): The students's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation of the Student.

        If attrs is a list of strings, only those attributes
        are included.
        Otherwise, all attributes are returned.
        """
        if isinstance(attrs, list) and all(isinstance(
                attr, str) for attr in attrs):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance using a dictionary.

        Args:
            json (dict): Dictionary with new attribute values.
        """

        for key, value in json.items():
            setattr(self, key, value)
