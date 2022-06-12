#!/usr/bin/python3
""" Area and Perimeter"""


class Rectangle:
    """class Rectangle"""

    def __init__(self, width=0, height=0):

        self.height = height
        self.width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0

        return (2 * self.__width) + (self.__height * 2)

    @property
    def width(self):

        return self.__width

    @width.setter
    def width(self, value):

        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):

        return self.__height

    @height.setter
    def height(self, value):

        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):

        return self.width * self.height

    def perimeter(self):

        if self.__width == 0 or self.__height == 0:
            return 0

        return (2 * self.__width) + (self.__height * 2)

    def __str__(self):

        if self.__width == 0 or self.__height == 0:
            return ""

        return ((("#" * self.__width + "\n") * self.__height))[:-1]

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):

        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __str__(self):
        tot = ""
        for i in range(self.__height):
            tot += ("#" * self.__width + "\n")
            if i == self.__height - 1:
                tot = tot[:-1]
        return tot
