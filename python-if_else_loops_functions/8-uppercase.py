#!/usr/bin/python3
def upppercase(str):
    for char in str:
        if ord('a') <= ord(char) <= ord('z'):
            char = chr(ord(char) - 32)
        print("{:s}".format(char), end="")
        print()
