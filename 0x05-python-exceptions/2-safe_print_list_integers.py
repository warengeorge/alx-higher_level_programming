#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    list_len = 0
    for i in range(list_len, x):
        try:
            print("{:d}".format(my_list[i]), end='')
            list_len += 1
        except (ValueError, TypeError):
            pass
    print()
    return list_len
