#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if not my_list:
        return None
    if idx > 0 and len(my_list) > idx:
        new_list = my_list.copy()
        new_list[idx] = element
        return new_list
    return my_list
