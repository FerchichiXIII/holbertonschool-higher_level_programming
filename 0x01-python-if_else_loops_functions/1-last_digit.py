#!/usr/bin/python3
from ast import If
import random
number = random.randint(-10000, 10000)
if number < 0:
    last = number % -10
if number > 0:
    last = number % 10
if last > 5:
    print("Last digit of", number, "is", last, "and is greater than 5")
if last == 0:
    print("Last digit of", number, "is", last, "and is 0")
if last < 6:
    if last != 0:
        print("Last digit of", number, "is", last,
              "and is less than 6 and not 0")
