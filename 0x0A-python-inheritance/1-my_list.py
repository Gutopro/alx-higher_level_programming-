#!/usr/bin/python3
<<<<<<< HEAD
"""MyList
=======
"""
contains the MyList class
>>>>>>> 6f454e44fcc976de9a64fb238fc6afb3553c896a
"""


class MyList(list):
<<<<<<< HEAD
    """Contains list
    """

    def print_sorted(self):
        """Prints self in sorted format
        """

=======
    """a subclass of list"""
    def __init__(self):
        """initializes the object"""
        super().__init__()

    def print_sorted(self):
        """prints the sorted list"""
>>>>>>> 6f454e44fcc976de9a64fb238fc6afb3553c896a
        print(sorted(self))
