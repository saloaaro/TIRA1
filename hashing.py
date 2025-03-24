def hash_value(string):
    x = 23
    y = 2**32
    z = len(string)
    result = 0

    for i in range(z):
        n = ord(string[i]) - ord("a")
        result += n * x ** (z - i - 1)

    return result % y

if __name__ == "__main__":
    print(hash_value("abc")) # 25
    print(hash_value("kissa")) # 2905682
    print(hash_value("aybabtu")) # 154753059
    print(hash_value("tira")) # 235796
    print(hash_value("zzzzzzzzzz")) # 2739360440
