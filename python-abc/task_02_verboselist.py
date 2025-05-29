#!/usr/bin/env python3

from abc import ABC, abstractmethod


"""
This module defines the Verboselist class, which extends the functionality
of the class 'list' in Python to print messages when you deleter or fix
elements.
"""

class Verboselist(list):
    """
    Class that extends 'list' to notify when it has changes.
    """

    def append(self, item):
        """
        Adds an element to the list, and show a message.
        
        :param item: Element to add.
        """
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """
        Adds multiple elements to the list and show a message.
        :param iterable: Colection of elements to add.
        """
        count = len(list(iterable))
        super().extend(iterable)
        if count > 0:
            print(f"Extended the list with [{count}] items.")

    def remove(self, item):
        """
        Elimantes an element from the list and shows a message.
        
        :param item: Element to eliminate.
        """
        if item in self:
            print(f"Removed [{item}] from the list.")
            super().remove(item)
        else:
            print(f"Item [{item}] not found in the list.")

    def pop(self, index=-1):
        """
        Eliminates an element from the list by index and show a message.
        
        :param index: Index from the element to eliminate (has a defect, last one).
        :return: Eliminated element or none if list is empty.
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

    v1.append(4) # "added [4] to the list."
    v1.extend([5, 6]) # "Extended the list within [2] items."
    v1.remove(2) # "Removed [2] from the list."
    v1.pop() # "Popped [6] from the list."
    v1.pop(0) # "Popped [1] from the list."
