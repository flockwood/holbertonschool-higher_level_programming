#!/usr/bin/python3

"""Define a class named Mylist"""


class MyList(list):
    """Mylist inherits from list

    Args:
        list: list class
    """

    def print_sorted(self):
        """Prints the list, but sorted(ascending sort)"""
        print(sorted(self))
