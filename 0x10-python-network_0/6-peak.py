#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    if not list_of_integers:
        return None

    def my_peak(nums, low, high):
        mid = (low + high) // 2
        if (mid == 0 or nums[mid] >= nums[mid - 1]) and\
                (mid == len(nums) - 1 or nums[mid] >= nums[mid + 1]):
            return nums[mid]
        elif mid > 0 and nums[mid - 1] > nums[mid]:
            return my_peak(nums, low, mid - 1)
        else:
            return my_peak(nums, mid + 1, high)

    return my_peak(list_of_integers, 0, len(list_of_integers) - 1)
