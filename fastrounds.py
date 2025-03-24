def count_rounds(numbers):
    rounds = 1  # Aloitamme ensimmäisestä kierroksesta
    max_seen = numbers[0]  # Seuraa suurinta tähän asti nähtyä lukua

    for i in range(1, len(numbers)):
        if numbers[i] < numbers[i - 1]:  # Järjestys katkeaa -> uusi kierros
            rounds += 1
        max_seen = max(max_seen, numbers[i])  # Päivitä suurin nähty luku

    return rounds

# Testataan funktiota
if __name__ == "__main__":
    print(count_rounds([1, 2, 3, 4]))  # 1
    print(count_rounds([1, 3, 2, 4]))  # 2
    print(count_rounds([4, 3, 2, 1]))  # 4
    print(count_rounds([1]))  # 1
    print(count_rounds([2, 1, 4, 7, 5, 3, 6, 8]))  # 4
    print(count_rounds([3, 1, 2]))  # 2
    print(count_rounds([2, 5, 4, 1, 3]))  # 4

    # Suuri testitapaus
    n = 10**5
    numbers = list(reversed(range(1, n+1)))
    print(count_rounds(numbers))  # 100000
