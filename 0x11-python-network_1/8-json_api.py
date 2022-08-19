#!/usr/bin/python3
"""
takes in a letter and sends a POST request
 to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    data = {'q': q}
    r = requests.post(url, data=data)
    try:
        r_json = r.json()
        if len(r_json) == 0:
            print("No result")
        else:
            print("[{}] {}".format(r_json['id'], r_json['name']))
    except ValueError:
        print("Not a valid JSON")
