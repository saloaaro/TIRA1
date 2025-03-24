def find(s):
    # Initialise an empty set to store unique characters in the string
    unique_chars = set()

    # Initialise an empty list to store the result
    result = []

    # Initialise an empty string to store the current longest non-repetitive string
    longest_non_repetitive_string = ""

    # Initialise an empty string to store the current longest repetitive string
    longest_repetitive_string = ""

    # Iterate through each character in the string
    for char in s:
        # If the character is already in the set, it means the current string has already been seen before
        if char in unique_chars:
            # If the current longest non-repetitive string is longer than the longest repetitive string,
            # update the longest repetitive string to be the longest non-repetitive string
            if len(longest_non_repetitive_string) > len(longest_repetitive_string):
                longest_repetitive_string = longest_non_repetitive_string

            # Update the current longest non-repetitive string to be the current string
            longest_non_repetitive_string = char

            # If the current string is not the same as the current longest non-repetitive string,
            # update the current longest non-repetitive string to be the current string
            if char != longest_non_repetitive_string:
                longest_non_repetitive_string = char
        else:
            # If the character is not already in the set, add it to the set
            unique_chars.add(char)

        # If the current longest non-repetitive string is longer than the longest repetitive string,
        # update the longest repetitive string to be the longest non-repetitive string
        if len(longest_non_repetitive_string) > len(longest_repetitive_string):
            longest_repetitive_string = longest_non_repetitive_string

    # The result is the length of the longest repetitive string
    result.append(len(longest_repetitive_string))

    return result

# Test
print(find("zzz"))  # 1
print(find("aybabtu"))  # 1
print(find("abcdefghijklmnopqrstuvwxyz"))  # 2




