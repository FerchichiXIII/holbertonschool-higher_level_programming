#!/usr/bin/python3
def read_file(filename="my_file_0.txt"):
    with open(filename, "r", encoding="UFT-8") as f:
        print(f.read())
