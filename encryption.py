def encrypt(s):
    aakkoset = "abcdefghijklmnopqrstuvwxyz"
    encrypted = ""
    for i, char in enumerate(s):
        if char.isalpha():
            idx = aakkoset.index(char)
            new_idx = (idx + i + 1) % 26
            encrypted += aakkoset[new_idx]
        else:
            encrypted += char
    return encrypted


if __name__ == "__main__":
    print(encrypt("abc")) # bdf
    print(encrypt("xz")) # yb
    print(encrypt("kkkkkkkk")) # lmnopqrs
    print(encrypt("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")) # bcdefghijklmnopqrstuvwxyzabcde