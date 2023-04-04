#!/usr/bin/env python3

"""
This script sends a request to a given URL and prints the value of the X-Request-Id
variable found in the header of the response.
"""

import sys
import urllib.request

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <URL>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]

    request = urllib.request.Request(url)

    try:
        with urllib.request.urlopen(request) as response:
            headers = dict(response.headers)
            x_request_id = headers.get("X-Request-Id")
            if x_request_id:
                print(x_request_id)
    except urllib.error.URLError as e:
        print("Error fetching page: {}".format(e.reason))
        sys.exit(1)
