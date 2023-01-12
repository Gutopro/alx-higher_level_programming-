#!/usr/bin/python3
# 0-square.py
"""This class defines a square object"""

class Square:
    """Represents a square"""
    pass
if __name__ == "__main__":
    Square = __import__('0-square').Square

    my_square = Square()
    print(type(my_square))
    print(my_square.__dict__)
