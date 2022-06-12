#!/usr/bin/python3
def uniq_add(my_list=[]):
    n = set(my_list)
    a = 0
    for i in n:
        a = a+i
    return a
