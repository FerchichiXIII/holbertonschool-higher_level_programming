#!/usr/bin/python3
""""my list"""


class MyList(list):

    """class mylist"""

    def print_sorted(self):
        print(sorted(list(self)))
