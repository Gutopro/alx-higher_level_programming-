#!/usr/bin/python3
import urllib.request

# Define the URL to fetch
url = 'https://alx-intranet.hbtn.io/status'

# Open the URL using a with statement
with urllib.request.urlopen(url) as response:
    # Read the response body
    body = response.read()

    # Display the response body in the required format
    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
    print("\t- utf8 content: {}".format(body.decode('utf-8')))
