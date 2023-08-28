#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    R = []
    k = 0
    try:
        for b in range(list_length):
            try:
                if isinstance(my_list_1[b], str) or\
                        isinstance(my_list_2[b], str):
                    k = 0
                    print("wrong type")
                elif my_list_2[b] == 0:
                    k = 0
                    print("division by 0")
                else:
                    k = my_list_1[b] / my_list_2[b]

            except IndexError:
                k = 0
                print("out of range")
            except TypeError:
                pass
            except ZeroDivisionError:
                pass
            R.append(k)
    finally:
        return (R)
