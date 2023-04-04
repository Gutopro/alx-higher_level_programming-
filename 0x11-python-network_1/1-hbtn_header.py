#!/usr/bin/python3
import urllib.request
import sys

# Get the URL from the command line arguments
url = sys.argv[1]

# Open the URL using a with statement
with urllib.request.urlopen(url) as response:
    # Get the value of the X-Request-Id header
    x_request_id = response.getheader('X-Request-Id')

    # Display the X-Request-Id header value
    print(x_request_id)
