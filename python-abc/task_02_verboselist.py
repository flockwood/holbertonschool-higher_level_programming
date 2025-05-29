#!/usr/bin/env python3

class VerboseList(list):
    """
    A list subclass that prints notifications when modified via
    append, extend, remove, or pop.
    """

    def append(self, item):
        """Add an element and notify."""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """Add multiple elements and notify."""
        items = list(iterable)
        count = len(items)
        super().extend(items)
        print(f"Extended the list with [{count}] items.")

    def remove(self, item):
        """Remove an element and notify, or show a warning if not found."""
        if item in self:
            print(f"Removed [{item}] from the list.")
            super().remove(item)
        else:
            print(f"Item [{item}] not found in the list.")

    def pop(self, index=-1):
        """Remove and return element by index, or show a warning if list is empty."""
        if len(self) == 0:
            print("Cannot pop from an empty list.")
            return None
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)


# Testing the VerboseList
if __name__ == "__main__":
    vl = VerboseList([1, 2, 3])
    vl.append(4)          # "Added [4] to the list."
    vl.extend([5, 6])     # "Extended the list with [2] items."
    vl.remove(2)          # "Removed [2] from the list."
    vl.remove(10)         # "Item [10] not found in the list."
    vl.pop()              # "Popped [6] from the list."
    vl.pop(0)             # "Popped [1] from the list."
    empty_list = VerboseList()
    empty_list.pop()      # "Cannot pop from an empty list."
