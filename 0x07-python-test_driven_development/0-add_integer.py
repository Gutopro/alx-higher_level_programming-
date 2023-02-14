#!/usr/bin/python3

"""
Example script that demonstrates the use of the add_integer function.
"""

# Import the add_integer function from the 0-add_integer module
add_integer = __import__('0-add_integer').add_integer

# Call the add_integer function with various arguments and print the results
print(add_integer(1, 2))
print(add_integer(100, -2))
print(add_integer(2))
print(add_integer(100.3, -2))

# Catch and print any exceptions raised by the add_integer function
try:
    print(add_integer(4, "School"))
except Exception as e:
    print(e)
try:
    print(add_integer(None))
except Exception as e:
    print(e)
