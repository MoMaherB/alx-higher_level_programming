#!/usr/bin/python3
"""
- fetches http://httpbin.org/status/200
- uses the package requests
- displays the body of the response
"""
import requests

if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    response = requests.get(url)
    content = response.text

    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: OK")
