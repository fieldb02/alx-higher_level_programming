#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add
    a = 10
    b = 5
    addition = add(a, b)
    print ("{} + {} = {}".format(a, b, addition))

    from calculator_1 import sub
    a = 10
    b = 5
    subtract = sub(a, b)
    print("{} - {} = {}".format(a, b, subtract))

    from calculator_1 import mul
    a = 10
    b = 5
    multiply = mul(a, b)
    print ("{} * {} = {}".format(a, b, multiply))

    from calculator_1 import div
    a = 10
    b = 5
    division = div(a, b)
    print("{} / {} = {}".format(a, b, division))
