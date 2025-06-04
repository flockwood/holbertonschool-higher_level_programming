#!/usr/bin/python3


"""
This module defines a single function, append_write.

The function appends a string to the end of a UTF-8 encoded text file
and returns the number of characters added. The file is created if it
doesn't exist.
"""


def append_write(filename="", text=""):
    """
    Append a string to the end of a UTF-8 file and return characters added.
    
    The function creates the file if it doesn't exist, or appends to the
    end of the file if it already exists.

    Args:
        filename (str): The name of the file to append to.
        text (str): The string content to append to the file.

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(text)
        return len(text)
