#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    h = dir(hidden_4)
    for a in h:
        if "__" not in a:
            print(a)
