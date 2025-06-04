#!/usr/bin/python3

"""
This module defines a single function, write_file.

The function writes a string to a UTF-8 encoded text file and returns
the number of characters written. The file is created is it doesn't exist,
or overwritten if it does exist.
"""


def write_file(filename="", text=""):
    """
    Write a string to a UTF-8 text file and return characters written.
    
    the function creates the file it if doesn't exist, or overwrites
    the content if the file already exists.
    
    Args:
        filename (str): The name of the file to write to.
        text (str): The string content to write to the file.
        
    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)
        return len(text)
