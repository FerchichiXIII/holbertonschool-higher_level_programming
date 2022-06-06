#!/usr/bin/python3
from models.base import Base
"""First Rectangle"""


class Rectangle(Base):
    """class import"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Base class"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Area first"""
        return self.__height * self.__width

    def display(self):
        """
        Display #0
        Display #1
        """
        if self.__y != 0:
            for i in range(self.__y):
                print()

        for j in range(self.__height):
            print((self.__x * " ") + (self.__width * "#"))

    def __str__(self):
        """__str__"""

        return "[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
                                                self.id, self.__x, self.__y,
                                                self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Update #0"""
        list = ["id", "width", "height", "x", "y"]
        if (args):
            for i in range(len(args)):
                setattr(self, list[i], args[i])
        else:
            for j in kwargs:
                setattr(self, j, kwargs[j])
