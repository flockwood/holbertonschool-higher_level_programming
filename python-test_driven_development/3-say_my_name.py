#!/usr/bin/python3

"""Defines a name-printing function"""


def say_my_name(first_name, last_name=""):
    """Prints "My name is <first name> <last name>".

    Args:
        first_name (str): the first name of the person.
        second_name (str): the last name of the person. Defaults empty string

    Raises:
    TypeError: if first or last name aren't strings
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
