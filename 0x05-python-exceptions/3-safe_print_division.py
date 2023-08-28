#!/usr/bin/python3
def safe_print_division(a, b):
    R = 0
    try:
        if a == 0 or b == 0:
            R = None
        R = a / b
    except ZeroDivisionError:
        pass
    finally:
        print("Inside result: {}".format(R))
    return (R)
