#!/usr/bin/python
def print_reversed_list_integer(my_list=[]):
    my_list = my_list[::-1]
    for i in range(0, len(my_list)):
        print(my_list[i])
