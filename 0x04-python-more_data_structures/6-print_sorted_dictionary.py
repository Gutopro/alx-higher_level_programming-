#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    # Get a list of the keys in the dictionary
    keys = list(a_dictionary.keys())

    # Sort the keys alphabetically
    keys.sort()

    # Iterate through the sorted keys and print the key-value pairs
    for key in keys:
        print(key, ":", a_dictionary[key])
