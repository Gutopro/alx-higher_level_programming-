#!/usr/bin/python3
def roman_to_int(roman_string):
    # Create a dictionary of Roman numerals and corresponding integer values
    roman_to_int_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    # Return 0 if roman_string is not a string or None
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    # Initialize result and index variables
    result = 0
    index = 0

    # Iterate through the characters in the string
    while index < len(roman_string):
        # Get the current character and the next character, if it exists
        current_char = roman_string[index]
        next_char = roman_string[index+1] if index < len(roman_string)-1
        else None

        # Check if the current character is a special case
        if current_char == "I" and next_char in ["V", "X"]:
            # Add the corresponding value to the result
            result += roman_to_int_dict[next_char] - roman_to_int_dict
            [current_char]
            # Skip the next character by incrementing the index by 2
            index += 2
        elif current_char == "X" and next_char in ["L", "C"]:
            result += roman_to_int_dict[next_char] - roman_to_int_dict
            [current_char]
            index += 2
        elif current_char == "C" and next_char in ["D", "M"]:
            result += roman_to_int_dict[next_char] - roman_to_int_dict
            [current_char]
            index += 2
        else:
            # If the current character is not a special case, add its value
            result += roman_to_int_dict[current_char]
            # Increment the index by 1
            index += 1

    return result
