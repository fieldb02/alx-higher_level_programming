#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    number = len(sys.argv) - 1
    if number == 0:
        print("{} arguments:".format(number))
    if number == 1:
        print("{} argument.".format(number))
    else:
        print("{} arguments:".format(number))
    for i, a in enumerate(sys.argv[1:]):
        print("{}: {}".format(i + 1, a))
