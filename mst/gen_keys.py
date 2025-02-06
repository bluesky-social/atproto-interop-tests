#!/usr/bin/env python3

"""
Helper script to output MST keys with different letter prefixes, at given heights. Eg:

    A0/asdf - at MST height 0
"""

import hashlib
import random

def height(key):
    h = hashlib.sha256(key).hexdigest()
    i = 0
    for c in h:
        if c > '4':
            return i*2
        if c != '0':
            return i*2+1
        i = i+1
    raise Exception("very suss")

def rand_key(letter, level):
    num = random.randint(0, 999999)
    return f"{letter}{level}/{num:06}".encode("utf8")

def gen_key(letter, level):
    while True:
        key = rand_key(letter, level)
        if height(key) == level:
            print(key.decode("utf-8"))
            return

if __name__=="__main__":
    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        for level in [0,1,2,3,4,5]:
            gen_key(letter, level)
