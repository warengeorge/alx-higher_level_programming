#!/usr/bin/python3
"""Fetches a header of a response from a URL."""
import sys
import requests


if __name__ == '__main__':
    if len(sys.argv) > 1:
        url = sys.argv[1]
        response = requests.get(url)
        if 'X-Request-Id' in response.headers:
            print(response.headers['X-Request-Id'])
