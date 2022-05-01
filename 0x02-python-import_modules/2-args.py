#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argNumber = len(argv) - 1
    print("{} ".format(argNumber), end='')
    if argNumber == 0:
        print("arguments.")
    elif argNumber == 1:
        print("argument:")
    else:
        print("arguments:")
    for arg in range(1, len(argv)):
        print("{:d}: {:s}".format(arg, argv[arg]))
