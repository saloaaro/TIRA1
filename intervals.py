import random

def count_nested(intervals):
    # Tee kopio alkuperäisestä listasta, jotta emme muuta alkuperäistä
    intervals_copy = intervals[:]
    
    # Lajitellaan väli alkuarvon mukaan (a) nousevasti,
    # ja jos alkuarvot ovat samat, lajitaan loppuarvon (b) mukaan laskevasti
    intervals_copy.sort(key=lambda x: (x[0], -x[1]))

    nested_count = 0
    # Käydään välejä läpi ja tarkistetaan, onko nykyinen väli aiemman sisällä
    for i in range(1, len(intervals_copy)):
        if intervals_copy[i][0] >= intervals_copy[i-1][0] and intervals_copy[i][1] <= intervals_copy[i-1][1]:
            nested_count += 1

    return nested_count

# Esimerkkejä
if __name__ == "__main__":
    print(count_nested([])) # 0
    print(count_nested([(1, 2)])) # 0
    print(count_nested([(1, 2), (3, 4)])) # 0
    print(count_nested([(1, 3), (2, 4)])) # 0
    print(count_nested([(1, 4), (2, 3)])) # 1
    print(count_nested([(1, 4), (1, 3)])) # 1
    print(count_nested([(1, 4), (2, 4)])) # 1
    print(count_nested([(1, 1), (1, 2), (1, 3)])) # 2
    print(count_nested([(1, 6), (2, 5), (3, 4)])) # 2
    print(count_nested([(1, 4), (2, 5), (3, 6)])) # 0

    # Testausta suuremmilla syötteillä
    intervals = [(x+1, x+3) for x in range(10**5)]
    random.shuffle(intervals)  # Muutetaan järjestystä vain kopiossa
    print(count_nested(intervals)) # 0

    intervals = [(x+1, 2*10**5-x) for x in range(10**5)]
    random.shuffle(intervals)  # Muutetaan järjestystä vain kopiossa
    print(count_nested(intervals)) # 99999

    # Testi epäonnistui aiemmin
    intervals = [(382, 406), (38, 75)]
    print(count_nested(intervals))  # 0

    # Testi epäonnistui aiemmin
    intervals = [(538, 788), (693, 771), (634, 738)]
    print(count_nested(intervals))  # 2
