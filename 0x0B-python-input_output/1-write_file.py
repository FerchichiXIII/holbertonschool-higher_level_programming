#!/usr/bin/python3
"""input output"""


def write_file(filename="", text=""):
    """
        Write to a file
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        f.write(text)
    return len(text)
