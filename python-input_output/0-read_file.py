#!/usr/bin/python3

"""
This module defines a single function, read_file.

The function reads a UTF-8 encoded text file and prints
its contents to stdout, exactly as it appears in
the file. No error handling is needed.
"""


def read_file(filename=''):
    """
    Read a UTF-8 text file and print it to stdout.

    Args:
        filename (str): The name of the file to read.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        print(content, end='')
