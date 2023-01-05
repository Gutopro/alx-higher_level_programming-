#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    # Create an empty set to store the result
    result_set = set()

    # Iterate through the elements in set_1
    for element in set_1:
        # If the element is not in set_2, add it to the result set
        if element not in set_2:
            result_set.add(element)

    # Iterate through the elements in set_2
    for element in set_2:
        # If the element is not in set_1, add it to the result set
        if element not in set_1:
            result_set.add(element)

    # Return the result set
    return result_set
