#!/usr/bin/python3
"""input output"""


def append_write(filename="", text=""):
    """
        Append to a file
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        f.write(text)
    return len(text)
