#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    # If idx is negative or out of range, return a copy of the original list
    if idx < 0 or idx >= len(my_list):
        return my_list.copy()

    # Create a new list based on the original list
    new_list = my_list.copy()
    # Replace the element at the specified index
    new_list[idx] = element
    return new_list
