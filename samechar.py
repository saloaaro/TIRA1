def count(s):
    n = len(s)
    count_same_char = 0
    current_count = 1
    current_char = s[0]

    for i in range(1, n):
        if s[i] == current_char:
            current_count += 1
        else:
            current_char = s[i]

    current_char = s[0]
    current_count = 1
    for i in range(1, n):
        if s[i] != current_char:
            current_count = 1
        else:
            current_count += 1

    current_char = s[0]
    current_count = 1
    for i in range(1, n):
        if s[i] == current_char:
            current_count += 1
        else:
            count_same_char += (current_count * (current_count + 1)) // 2
            current_char = s[i]
            current_count = 1

    count_same_char += (current_count * (current_count + 1)) // 2

    return count_same_char

if __name__ == "__main__":
    print(count("aaa"))  # 6
    print(count("abbbcaa"))  # 11
    print(count("abcde"))  # 5



