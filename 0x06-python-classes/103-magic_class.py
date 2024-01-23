#!/usr/bin/python3
"""Define MagicClass"""
import math


class MagicClass:
    """Magic Clsaa"""
    def __init__(self, radius=0):
        """instances of MagicClass."""
        self.__radius = 0
        if not isinstance(radius, int) and not isinstance(radius, float):
            raise TypeError("radius must be a number")
        else:
            self.__radius = radius

    def area(self):
        """Returns area"""
        return math.pi * self.__radius ** 2

    def circumference(self):
        """Returns circumference"""
        return 2 * math.pi * self.__radius
