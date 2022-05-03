#!/usr/bin/python3
from hashlib import new
from re import I


def no_c(my_string):
    a = ""
    for i in my_string:
        if i is not "c" and i is not "C":
            a += i
    return a
