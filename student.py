import re

def check_number(number):
    if not re.match("^0[0-9]{8}$", number):
        return False

    paino = [3, 7, 1, 3, 7, 1, 3, 7]
    tulos = 0
    for pos in range(8):
        tulos += paino[pos] * int(number[pos])

    vika = (10 - tulos % 10) % 10
    return int(number[-1]) == vika

if __name__ == "__main__":
    print(check_number("012749138")) # False
    print(check_number("012749139")) # True
    print(check_number("013333337")) # True
    print(check_number("012345678")) # False
    print(check_number("012344550")) # True
    print(check_number("1337")) # False
    print(check_number("0127491390")) # False
