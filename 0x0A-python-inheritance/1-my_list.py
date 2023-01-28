#!/usr/bin/python3

""" a class MyList that inherits from list"""

class MyList(list):
    """ a subclass of list"""
    
    def _init_(self):
        
        """ initialize oblect """
        super()._init_()
        
    """ MyList class has a single public instance method"""
    def print_sorted(self):
        print(sorted(self))
