#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    arr = my_list[:]
    for ind, val in enumerate(my_list):
        if val % 2 == 0:
            arr[ind] = True
        else:
            arr[ind] = False
    return(arr)
