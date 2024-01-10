#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    max_value = 0
    for k in a_dictionary:
        if a_dictionary[k] > max_value:
            max_value = a_dictionary[k]
            max_key = k
    return max_key
