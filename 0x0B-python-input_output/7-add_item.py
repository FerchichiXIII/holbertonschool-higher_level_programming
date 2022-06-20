#!/usr/bin/python3
""" input output """


from sys import argv
save_to_json_file = __import__("5-save_to_json_file.py").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file.py").load_from_json_file

filename = "add_item.json"

try:
    my_obj = load_from_json_file(filename)
except FileNotFoundError:
    res = []

save_to_json_file(res + argv[1:], filename)
