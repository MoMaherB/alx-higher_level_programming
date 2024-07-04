#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""

def find_peak(list_of_integers):
    if not list_of_integers:
        return None

    def my_peak(nums, low, high):
        if low == high:
            return nums[low]
        mid = (low + high) // 2
        if nums[mid] < nums[mid + 1]:
            return my_peak(nums, mid + 1, high)
        return my_peak(nums, low, mid)

    return my_peak(list_of_integers, 0, len(list_of_integers) - 1)