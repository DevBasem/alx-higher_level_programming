#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL, and
displays the value of the X-Request-Id variable found in the header.
"""

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        header_value = response.getheader('X-Request-Id')
        print(header_value)
