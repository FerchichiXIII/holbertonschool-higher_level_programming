#!/usr/bin/python3
"""Only sub class of"""


def inherits_from(obj, a_class):
    """returns True if the object is an instance of a class"""
    if a_class in list(obj.__class__.__mro__)[1:]:
        return True
    else:
        return False
