#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    list = my_list[::-1]
    for i in range(0, len(list)):
        print("{:d}".format(i))
