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
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position
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
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    """
        Getter for position
    """
    @property
    def position(self):
        return self.__position
    """
        setter for position
    """
    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or len(value) != 2 or
                not isinstance(value[0], int) or value[0] < 0 or
                not isinstance(value[1], int) or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """print the square with the giving size  if zero draw newline"""
        if self.__size == 0:
            print("")
            return

        for lines in range(self.__position[1]):
            print("")
        for i in range(self.size):
            for k in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            print("")

    def __str__(self):
        """print the square with the print instance itself"""
        if self.__size != 0:
            for lines in range(self.__position[1]):
                print("")
        for i in range(self.__size):
            for k in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            if i != self.__size - 1:
                print("")
        return ("")
