#!/usr/bin/python3
from zmq import NULL


def uniq_add(my_list=[]):
    n = set(my_list)
    a = NULL
    for i in n:
        a = a+i
    return a
