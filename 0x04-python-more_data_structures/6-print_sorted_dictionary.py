#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    # Sort the keys alphabetically
    sorted_keys = sorted(a_dictionary.keys())

    # Iterate over the sorted keys
    for key in sorted_keys:
        # Print the key and its corresponding value
        print("{}: {}".format(key, a_dictionary[key]))
