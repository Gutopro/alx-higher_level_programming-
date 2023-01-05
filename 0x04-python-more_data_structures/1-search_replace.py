#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # Create a new list
    new_list = []

    # Iterate through each element in the list
    for element in my_list:
        # If the element is the search element,append the replace element
        if element == search:
            new_list.append(replace)
        # Otherwise, append the element to the new list
        else:
            new_list.append(element)

    return new_list
