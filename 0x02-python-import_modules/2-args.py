#!/usr/bin/python3
import sys
if __name__ == "__main__":
    x = len(sys.argv)
    if x == 1:
        print("{:d} {}.".format(0, "arguments"))
    elif x == 2:
        print("{:d} {}:".format(1, "argument"))
        for i in range(1, x):
            print("{:d}: {}".format(x - 1, sys.argv[i]))
    else:
        print("{:d} {}:".format(x - 1, "arguments"))
        for i in range(1, x):
            print("{:d}: {}".format(i, sys.argv[i]))
