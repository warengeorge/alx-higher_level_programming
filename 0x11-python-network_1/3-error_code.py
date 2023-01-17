#!/usr/bin/python3
"""Sends a request to a URL and prints its response or error code."""
import sys
from urllib import request, error


if __name__ == '__main__':
    if len(sys.argv) > 1:
        url = sys.argv[1]
        try:
            with request.urlopen(url) as response:
                print(response.read().decode('utf-8'))
        except error.HTTPError as ex:
            print('Error code: {}'.format(ex.code))
