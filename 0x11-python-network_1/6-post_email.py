#!/usr/bin/python3
"""
- takes in a URL,
- sends a request to the URL and displays the value
- of the X-Request-Id variable found in the header ofthe response.
"""
import urllib.request
import sys

if __name__ == "__main__":
    arg_url = sys.argv[1]

    req = urllib.request.Request(arg_url)
    with urllib.request.urlopen(req) as res:
        print(dict(res.headers).get("X-Request-Id"))
