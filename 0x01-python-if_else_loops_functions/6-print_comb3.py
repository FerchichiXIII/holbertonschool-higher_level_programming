#!/usr/bin/python3
for a in range(0, 9):
    for b in range(a+1, 10):
        if b < 9:
            print("{}{}".format(a, b), end=', ')
print("{}{}".format(a, b))
