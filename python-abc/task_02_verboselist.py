#!/usr/bin/env python3

from abc import ABC, abstractmethod

"""
This module defines the Verboselist class, which extends the functionality
of Python's built-in 'list' class to print messages when elements are
added or removed.
"""


class Verboselist(list):
    """
    A list subclass that provides verbose output for certain list operations.
    """

    def append(self, item):
        """
        Add an element to the list and print a message.

        :param item: Element to add.
        """
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """
        Add multiple elements to the list and print a message.

        :param iterable: Collection of elements to add.
        """
        count = len(list(iterable))
        super().extend(iterable)
        if count > 0:
            print(f"Extended the list with [{count}] items.")

    def remove(self, item):
        """
        Remove an element from the list and print a message.

        :param item: Element to remove.
        """
        if item in self:
            print(f"Removed [{item}] from the list.")
            super().remove(item)
        else:
            print(f"Item [{item}] not found in the list.")

    def pop(self, index=-1):
        """
        Remove and return an element from the list by index,
        printing a message.

        :param index: Index of the element to remove (default is last).
        :return: Removed element, or None if the list is empty.
        """
        if self:
            item = super().pop(index)
            print(f"Popped [{item}] from the list.")
            return item
        else:
            print("Cannot pop from an empty list.")
            return None


if __name__ == "__main__":
    v1 = Verboselist([1, 2, 3])

    v1.append(4)         # "Added [4] to the list."
    v1.extend([5, 6])    # "Extended the list with [2] items."
    v1.remove(2)         # "Removed [2] from the list."
    v1.pop()             # "Popped [6] from the list."
    v1.pop(0)            # "Popped [1] from the list."
