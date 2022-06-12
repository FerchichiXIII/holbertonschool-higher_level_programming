#!/usr/bin/python3
def multiple_returns(sentence):
    a = len(sentence)
    if a == 0:
        c = None
    else:
        c = sentence[0]
    mul = (a, c)
    return mul
