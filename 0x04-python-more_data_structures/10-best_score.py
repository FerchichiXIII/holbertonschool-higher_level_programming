#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        return None
    mmax_key = max(a_dictionary, key=a_dictionary.get)
    return mmax_key