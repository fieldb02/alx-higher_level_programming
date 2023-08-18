#!/usr/bin/python3
def uniq_add(my_list=[]):
    a = set(my_list)
    addition = 0
    for i in a:
        addition += i
    return (addition)
