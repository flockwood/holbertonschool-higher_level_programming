#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i, value in enumerate(row):
            if i != 0:
                print(" ", end="")
            print("{:d}".format(value), end="")
        print()
