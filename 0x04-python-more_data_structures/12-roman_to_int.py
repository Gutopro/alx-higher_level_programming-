#!/usr/bin/python3
def roman_to_int(roman_number):
    # Create a dictionary that maps Roman numerals to integers
    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    # Initialize a result variable to store the integer value of the Roman num
    result = 0

    # Loop through the characters in the Roman numeral from left to right
    for i in range(len(roman_number)):
        # Get the integer value of the current Roman numeral
        current_numeral = roman_dict[roman_number[i]]

        # If the next numeral is larger, it means that the current numeral
        # So we subtract the current numeral from the result
        if i + 1 < len(roman_number) and roman_dict[roman_number[i+1]] >
        current_numeral:
            result -= current_numeral
        # Otherwise, we add the current numeral to the result
        else:
            result += current_numeral

    # Return the result
    return result
