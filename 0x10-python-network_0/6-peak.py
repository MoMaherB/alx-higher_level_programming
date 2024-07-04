#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Finds a peak in list_of_integers"""

    if not list_of_integers:
        return None

    def find_peak_recursive(nums, low, high):
        if low == high:
            return nums[low]

        mid = (low + high) // 2

        if mid < len(nums) - 1 and nums[mid] < nums[mid + 1]:
            return find_peak_recursive(nums, mid + 1, high)
        if mid > 0 and nums[mid] < nums[mid - 1]:
            return find_peak_recursive(nums, low, mid - 1)
        return nums[mid]

    return find_peak_recursive(list_of_integers, 0, len(list_of_integers) - 1)
