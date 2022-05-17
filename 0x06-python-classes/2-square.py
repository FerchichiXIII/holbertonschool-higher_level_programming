#!/usr/bin/python3
""" Square with size"""


class Square:
    """class square"""

    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be an integer")
        self.__size = size
