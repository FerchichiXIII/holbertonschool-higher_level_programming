#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        if value is int:
            return True
        else:
            return False
    except:
        Exception
        print("Unknown format code 'd' for object of type 'str'")
    print("{:d}".format(value))
