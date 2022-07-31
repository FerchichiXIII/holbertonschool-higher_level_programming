#!/usr/bin/python3
"""0x0A - 100-my_int.py"""

class My_Int(int):
    """class my_int"""

    def __eq__(self, other):
        """eq"""
        return super().__ne__(other)

    def __ne__(self, other):
        """ne"""
        return super().__eq__(other)
