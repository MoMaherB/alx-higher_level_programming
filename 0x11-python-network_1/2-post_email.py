#!/usr/bin/python3
"""
- takes in a URL
- sends a POST request to the passed URL
- takes email as a parameter
- displays the body of the response
"""
import sys
from urllib import parse
from urllib import request


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    data = parse.urlencode(value).encode("ascii")

    req = request.Request(url, data)
    with request.urlopen(req) as response:
        print(response.read().decode("utf-8"))