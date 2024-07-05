#!/usr/bin/python3
"""
fetches https://alx-intranet.hbtn.io/status.uses urlib package
"""


if __name__ == '__main__':
    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as result:
        responce = result.read()
        print("Body response:")
        print("\t- type: {}".format(type(responce)))
        print("\t- content: {}".format(responce))
        print("\t- utf8 content: {}".format(responce.decode('utf-8')))