#!/usr/bin/python3
"""Fetches a header of a response from a URL."""
import sys
from urllib import request


if __name__ == '__main__':
    if len(sys.argv) > 1:
        url = sys.argv[1]
        with request.urlopen(url) as response:
            print(response.headers['X-Request-Id'])
