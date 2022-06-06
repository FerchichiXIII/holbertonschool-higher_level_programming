#!/usr/bin/python3
from models.rectangle import Rectangle
"""And now, the Square!"""


class Square(Rectangle):
    """Class Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(size, size, x, y, id)
