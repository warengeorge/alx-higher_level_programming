#!/usr/bin/python3
import sys
if __name__ == "__main__":
    arg_len = len(sys.argv)
    res = 0
    for i in range(1, arg_len):
        res += int(sys.argv[i])
    print(res)
