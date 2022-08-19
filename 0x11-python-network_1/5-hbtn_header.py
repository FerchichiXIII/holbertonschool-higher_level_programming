#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and displays
 the value of the variable X-Request-Id in the response header
"""

import sys
from urllib import request

if __name__ == "__main__":
    with request.urlopen(sys.argv[1]) as response:
        print(response.getheader('X-Request-Id'))
