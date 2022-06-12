#!/usr/bin/python3
""" Area of a square """


class Square:
    """class square"""

    def __init__(self, size=0):
        """initialsation"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """area"""
        return self.__size * self.__size
