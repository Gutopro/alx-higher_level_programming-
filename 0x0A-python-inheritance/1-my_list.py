#!/usr/bin/python3

class MyList(list):
    """ MyList class has a single public instance method"""
    def print_sorted(self):
        print(sorted(self))
