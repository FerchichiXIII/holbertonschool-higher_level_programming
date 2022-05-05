#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    n_list = my_list[:]
    if my_list == 0:
        return None
    for i in range(0, len(n_list)):
        if i % 2 == 0:
            n_list[i] = True
        else:
            n_list[i] = False
    return n_list
