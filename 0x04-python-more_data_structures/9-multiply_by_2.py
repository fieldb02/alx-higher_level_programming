#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = {}

    for key, i in dict.items(a_dictionary):
        i *= 2
        new[key] = i
    return (new)
