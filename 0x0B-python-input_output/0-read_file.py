#!/usr/bin/python3
def read_file(filename="my_file_0.txt"):
    with open(filename) as f:
        print(f.read())
