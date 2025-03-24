def find(s):
    unique_chars = set()
    result = []
    longest_non_repetitive_string = ""

    longest_repetitive_string = ""

    for char in s:
        if char in unique_chars:
            if len(longest_non_repetitive_string) > len(longest_repetitive_string):
                longest_repetitive_string = longest_non_repetitive_string

            longest_non_repetitive_string = char

            if char != longest_non_repetitive_string:
                longest_non_repetitive_string = char
        else:
            unique_chars.add(char)

        if len(longest_non_repetitive_string) > len(longest_repetitive_string):
            longest_repetitive_string = longest_non_repetitive_string

    result.append(len(longest_repetitive_string))

    return result

print(find("zzz"))  # 1
print(find("aybabtu"))  # 1
print(find("abcdefghijklmnopqrstuvwxyz"))  # 2




