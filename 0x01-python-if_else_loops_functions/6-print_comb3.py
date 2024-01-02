#!/usr/bin/python3
for i in range(0, 9):
    for j in range(1 + i, 10):
        if i != 8:
            print("{:d}{:d}".format(i, j), end=", ")
        else:
            print("{:d}{:d}".format(i, j), end="\n")
