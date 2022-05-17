#!/usr/bin/python3
""" Size validation """


class Square:
    """class square"""

    def __init__(self, size=0):
        """def __init___"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be an integer")
        self.__size = size
