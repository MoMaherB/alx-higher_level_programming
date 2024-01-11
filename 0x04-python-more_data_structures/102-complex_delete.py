#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    carpage = []
    for key in a_dictionary:
        if a_dictionary[key] == value:
            carpage.append(key)
    for carp in carpage:
        del a_dictionary[carp]
    return a_dictionary
