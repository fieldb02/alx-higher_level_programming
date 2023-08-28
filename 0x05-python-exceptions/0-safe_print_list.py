#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        k = 0
        for b in range(x):
            print(my_list[b], end="")
            k += 1
    except IndexError:
        pass
    print()
    return (k)
