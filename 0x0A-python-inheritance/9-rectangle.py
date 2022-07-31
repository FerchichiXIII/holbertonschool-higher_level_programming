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
