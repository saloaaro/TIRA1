def count(s):
    ones = s.count('1')
    zeros = s.count('0')
    return ones * (ones - 1) // 2 + zeros * (zeros - 1) // 2

if __name__ == "__main__":
    print(count("0101"))  # 2
    print(count("000000"))  # 15
    print(count("000111"))  # 6
    print(count("00100001101100"))  # 46
