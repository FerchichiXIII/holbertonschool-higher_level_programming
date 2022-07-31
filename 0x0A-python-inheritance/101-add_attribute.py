#!/usr/bin/python3
"""
dds a new attribute
 to an object if it’s possible
 """

def add_attribute(obj, Attribute, value):
    """add_attribute"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, Attribute, value)
