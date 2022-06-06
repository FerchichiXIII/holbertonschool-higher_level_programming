#!/usr/bin/python3
"""First Rectangle"""
from models.base import Base


class Rectangle(Base):
    """class import"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Base class"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Width of this rectangle"""
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """Height of this rectangle"""
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @property
    def x(self):
        """X of this rectangle"""
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
        """Y of this class rectangle"""
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
        return self.height * self.width

    def display(self):
        """Display"""
        if self.y != 0:
            for i in range(self.y):
                print()

        for j in range(self.height):
            print((self.x * " ") + (self.width * "#"))

    def __str__(self):
        """__str__"""

        return "[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
                                                self.id, self.x, self.y,
                                                self.width, self.height)

    def update(self, *args, **kwargs):
        """Update"""
        list = ["id", "width", "height", "x", "y"]
        if (args):
            for i in range(len(args)):
                setattr(self, list[i], args[i])
        else:
            for j in kwargs:
                setattr(self, j, kwargs[j])
