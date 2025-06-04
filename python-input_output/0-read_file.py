#!/usr/bin/python3

"""
This modile defines a single function, read_file
which reads a UTF-8 encoded text file and prints 
its contents to stdout, exactly as it appears on
the file. No error handling is needed.
"""


def read_file(filename=''):
    """
    Reads a UTF-8 text file and prints it to stdout.

    Args:
        filename (str): The name of the file to read
    """
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        print(content, end='')
