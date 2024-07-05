#!/usr/bin/python3
"""
- fetches http://httpbin.org/status/200
- uses the package requests
- displays the body of the response
"""
import requests

if __name__ == "__main__":
    url = "http://httpbin.org/status/200"
    response = requests.get(url)
    content = "OK" if response.status_code == 200 else response.text

    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))
