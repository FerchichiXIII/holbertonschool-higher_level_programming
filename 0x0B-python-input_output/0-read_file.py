#!/usr/bin/python3
"""input output"""


def read_file(filename=""):
    """
    read_file function
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        read_file = f.read()
        print(read_file, end="")
