#!/usr/bin/python3
print_list_integer = __import__('0-print_list_integer').print_list_integer
def print_list_integer(my_list=[]):
    print(*my_list, sep="\n")
