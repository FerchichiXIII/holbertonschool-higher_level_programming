#!/usr/bin/python3
from asyncore import read


def read_file(filename=""):
    with open(filename) as f:
        contents = f.read()
    print(contents)
