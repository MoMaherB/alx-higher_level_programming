#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None:
        return 0
    score = 0
    weight = 0
    for tup in my_list:
        score += tup[0] * tup[1]
        weight += tup[1]
    return score / weight
