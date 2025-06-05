#!/usr/bin/python3


"""
This module defines a Student class.

The Student class represents a student with basic information and provides
a method to get a dictionary representation for JSPN serialization.
"""


class Student:
    """
    Student class that defines a student by basic information.

    Public instance attributes: first_name, last_name, age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize a Student instance.

        Args:
            first_name (str): The student's first name.
            last_name(str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieve a dictionary representation of a Student instance.

        Returns:
            dict: Dictionary containing all instance attributes.
        """
        return self.__dict__
