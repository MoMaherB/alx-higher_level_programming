#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None:
        return 0
    score = my_list[0][0] * my_list[0][1]
    weight = my_list[0][1]
    for i in range(1, len(my_list)):
        score += my_list[i][0] * my_list[i][1]
        weight += my_list[i][1]
    return score / weight
