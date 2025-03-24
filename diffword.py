def count(s):
    words = s.split()
    unique_words = set(words)
    return len(unique_words)

if __name__ == "__main__":
    print(count("apina apina apina"))  # 1
    print(count("apina banaani cembalo"))  # 3
    print(count("a b c a b c a b c"))  # 3
    print(count("saippuakauppias"))  # 1
