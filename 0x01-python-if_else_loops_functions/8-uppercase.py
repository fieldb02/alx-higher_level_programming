#!/usr/bin/python3
def uppercase(str):
    output = ""
    for n in str:
        if n in 'abcdefghijklmnopqrstuvwxyz':
            a = ord(n)
            b = a - 32
            b = chr(b)
            output += b
        else:
            output += n
    print("{}".format(output), end="")
    print()
