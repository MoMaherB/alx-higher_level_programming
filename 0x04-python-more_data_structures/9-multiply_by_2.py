#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    b_dict = a_dictionary.copy()
    for k in b_dict:
        b_dict[k] *= 2
    return b_dict
