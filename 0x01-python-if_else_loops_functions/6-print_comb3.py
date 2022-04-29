#!/usr/bin/python3
for a in range(0, 9):
    for b in range(a, 10):
        if b > a and a < 8:
            print("{}{}".format(a, b), end=', ')
print("{}{}".format(a, b))
