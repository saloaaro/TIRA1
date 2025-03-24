def count(s):
    total_count = 0
    count_a = 0

    for char in s:
        if char == 'a':
            count_a = 0
        else:
            count_a += 1
            total_count += count_a

    return total_count

if __name__ == "__main__":
    print(count("aaa"))  # 0
    print(count("saippuakauppias"))  # 23
    print(count("x"))  # 1
    print(count("aybabtu"))  # 20
    








