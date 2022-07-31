#!/usr/bin/python3
"""A Geometry class."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class square"""

    def __init__(self, size):
        """__init__"""
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)
