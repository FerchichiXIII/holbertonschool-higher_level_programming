#!/usr/bin/python3
"""input output"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """init"""
        self.first_name = first_name
        self.last_name = last_name
        self.ago = age

    def to_json(self):
        """convert object to json"""
        return self.__dict__
