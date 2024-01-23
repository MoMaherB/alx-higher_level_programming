#!/usr/bin/python3
"""Class Square"""


class Square:
    """Class Square
    Args:
        size: the size of the sauare
    Raises:
        TypeError: if the size is not int
        ValueError: if the size is less than zero
    """
    def __init__(self, size=0):
        if size != int(size):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    """
        method that return area based on size
        passed by the user
    """
    def area(self):
        return self.__size ** 2
