#!/usr/bin/python3
"""Class Square"""


from typing import Any


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
    """
        Getter function for the size
    """
    @property
    def size(self):
        return self.__size
    """
        Setter method to assign new value
        Args:
            new_Size: this is a new size
        Raise:
            TypeError and ValueError
    """
    @size.setter
    def size(self, new_size):
        if not isinstance(new_size, int):
            raise TypeError("size must be an integer")
        if new_size < 0:
            raise ValueError("size must be >= 0")
        self.__size = new_size
