#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    b_dict = sorted(a_dictionary)
    for k in b_dict:
        print(f"{k}: {a_dictionary[k]}")
