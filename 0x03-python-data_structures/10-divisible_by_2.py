#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    nlist = my_list[:]
    if my_list == 0:
        return None
    for i in range(0, len(nlist)):
        if i % 2 == 0:
            nlist[i] = True
        else:
            nlist[i] = False
    return nlist
