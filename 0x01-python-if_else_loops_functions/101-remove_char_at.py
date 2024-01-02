#!/usr/bin/python3
def remove_char_at(str, n):
    rmstr = ""
    for i in range(len(str)):
        if i != n:
            rmstr += str[i]

    return rmstr
