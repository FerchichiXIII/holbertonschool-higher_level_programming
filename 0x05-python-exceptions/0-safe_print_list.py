#!/usr/bin/python3
from distutils.log import error


def safe_print_list(my_list=[], x=0):
    i = 0
    pr = 0
    for i in range(0, x):
        try:
            print("{}".format(my_list[i]), end="")
            pr += 1
        except:
            error
            continue
    print()
    return pr
