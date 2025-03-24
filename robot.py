def count(s):
    x, y = 0, 0  
    ruudukko = set([(x, y)])  

    for move in s:
        if move == 'U':
            y += 1
        elif move == 'D':
            y -= 1
        elif move == 'L':
            x -= 1
        elif move == 'R':
            x += 1
        ruudukko.add((x, y))

    return len(ruudukko)

if __name__ == "__main__":
    print(count("LL"))  # 3
    print(count("UUDLRR"))  # 5
    print(count("UDUDUDU"))  # 2
