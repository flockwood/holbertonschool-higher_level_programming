#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if 1 < j:
            print("{:d}{:d}".format(i, j))
        else:
            print("{:d}{:d},".format(i, j), end="")
