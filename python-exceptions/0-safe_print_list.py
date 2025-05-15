#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            try:
                print(my_list[i], end="")
                count += 1
            except IndexError:
                break  # Stop printing when an out-of-range index is reached
    finally:
        print()  # Print a newline after printing elements
    return count
