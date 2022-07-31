#!/usr/bin/python3
"""Rectangle"""
base_geometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(base_geometry):
    """class rectangle"""

    def __init__(self, width, height):
        """init"""
        super().integer_validator('width', width)
        super().integer_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):
        """area"""
        return self.__width * self.__height

    def __str__(self):
        """str"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
