#!/usr/bin/python3
def remove_char_at(str, n):
    strcopy = ''
    if n > len(str) or n < 0:
        return str
    for ind in str:
        if ind != str[n]:
            strcopy += ind
    return strcopy
