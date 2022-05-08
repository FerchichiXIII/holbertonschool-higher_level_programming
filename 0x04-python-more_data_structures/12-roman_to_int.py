#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None:
        return 0
    num = 0
    roman_num = {'I': 1, 'V': 5, 'X': 10,'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for i in roman_string:
        num += roman_num.get(i, 0)
    sub = {"CM": -200, "XC": -20, 'IX': -2, 'CD': -200, "IV": -2, "XC": -20}
    char = ""
    for i in range(0, len(roman_string)-1):
        char = roman_string[i] + roman_string[i+1]
        if char in sub:
            num += sub[char]
    return num
