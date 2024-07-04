#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    if not list_of_integers:
        return None

    low = 0
    high = len(list_of_integers) - 1

    def find_peak_recursive(nums, low, high):
        if low == high:
            return nums[low]

        mid = (low + high) // 2

        if nums[mid] < nums[mid + 1]:
            return find_peak_recursive(nums, mid + 1, high)
        return find_peak_recursive(nums, low, mid)

    return find_peak_recursive(list_of_integers, low, high)


