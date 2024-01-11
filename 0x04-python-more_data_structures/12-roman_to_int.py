#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str:
        return 0
    rdic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    sum = rdic[roman_string[0]]
    for i in range(1, len(roman_string)):
        if rdic[roman_string[i]] <= rdic[roman_string[i - 1]]:
            sum = sum + roman_dict[roman_string[i]]
        else:
            sum = sum + rdic[roman_string[i]] - 2 * rdic[roman_string[i - 1]]
    return sum
