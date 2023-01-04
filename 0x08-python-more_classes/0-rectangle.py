#!/usr/bin/python3

"""
Module for defining a rectangle with a given width and height.

Classes:
- Rectangle: defines a rectangle with a given width and height.
"""

class Rectangle:
    """
    Defines a rectangle with a given width and height.

    Attributes:
    - width (int): The width of the rectangle.
    - height (int): The height of the rectangle.
    """
    pass

# Import the Rectangle class from the 0-rectangle module
Rectangle = __import__('0-rectangle').Rectangle

# Create an instance of the Rectangle class
my_rectangle = Rectangle()

# Print the type of the instance
print(type(my_rectangle))

# Print the instance's __dict__ attribute
print(my_rectangle.__dict__)
