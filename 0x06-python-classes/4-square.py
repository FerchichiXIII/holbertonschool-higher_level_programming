#!/usr/bin/python3
""" Access and update private attribute """


class Square:
    """class square"""

    def __init__(self, size=0):
        """initialsation"""
        self.__size = size

    def area(self):
        """area"""
        return self.__size * self.__size

    @property
    def size(self):
        """size"""
        return self.__size

    @size.setter
    def size(self, value):
        """size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            """value"""
            self.__size = value
