def count_splits(sequence):
    zero = sequence.count("0")
    one = sequence.count("1")

    if zero != one:
        return 0

    zero2 = one2 = 0
    result = 0

    for i in sequence:
        if i == "0":
            zero2 += 1
        if i == "1":
            one2 += 1

        if zero2 == one2:
            result += 1

    return result - 1

if __name__ == "__main__":
    print(count_splits("00")) # 0
    print(count_splits("01")) # 0
    print(count_splits("0110")) # 1
    print(count_splits("010101")) # 2
    print(count_splits("000111")) # 0
    print(count_splits("01100110")) # 3

    sequence = "01"*10**5
    print(count_splits(sequence)) # 99999
