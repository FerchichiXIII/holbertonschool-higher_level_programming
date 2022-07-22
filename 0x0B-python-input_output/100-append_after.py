#!/usr/bin/python3
"""input output"""


def append_after(filename="", search_string="", new_string=""):
    """
            appends a string at the end of each line containing
            the search string
    """
    with open(filename, 'r+') as f:
        lines = f.readlines()
        for i in range(len(lines)):
            if search_string in lines[i]:
                lines[i] += new_string
        f.seek(0)
        f.writelines(lines)
        f.truncate()
