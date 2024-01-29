#!/usr/bin/python3
"""Defines a class Rectangle"""


class Rectangle:
    """
    Class that defines properties of rectangle.
    width (int): width of the rectangle.
    height (int): height of the rectangle.
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """New instances of Rectangle.

        Args:
            width (int, optional): width of rectangle. Defaults to 0.
            height (int, optional): height of rectangle. Defaults to 0.
        """
        self.height = height
        self.width = width
        number_of_instances += 1

    @property
    def width(self):
        """Width.

        Returns:
            int: the width of the rectangle.
        """
        return self.__width

    @property
    def height(self):
        """Height.

        Returns:
            int: the height of the rectangle.
        """
        return self.__height

    @width.setter
    def width(self, value):
        """
        Setter for width of rectangle.

        Args:
            value : width of the rectangle.

        Raises:
            TypeError: if width is not an integer.
            ValueError: if width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """
            Setter for height of recyangle.

            Args:
                value (int): height of the rectangle.

            Raises:
                TypeError: if height is not an integer.
                ValueError: if height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
            Area of a rectangle.

            Returns: area.
        """
        return self.__height * self.__width

    def perimeter(self):
        """
            perimeter of a rectangle

            Returns: perimeter.
        """
        if self.__height == 0 or self.width == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)

    def __str__(self):
        """
            Prints the rectangle with the character # .

            Returns: print rectangle
        """
        rectangle = []

        if self.__width == 0 or self.__height == 0:
            return ""

        for i in range(self.__height):
            for j in range(self.__width):
                rectangle.append("#")
            rectangle.append("\n")

        rectangle.pop()

        return "".join(rectangle)

    def __repr__(self):
        """
        Returns a string representation of the rectangle.
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """
        Deletes an instance of a class
        """
        print("{:s}".format("Bye rectangle..."))
        number_of_instances -= 1
