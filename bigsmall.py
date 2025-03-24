def count_pairs(numbers):
    numbers = sorted(numbers)
    
    i, j = 0, 0
    pairs = 0
    n = len(numbers)
    
    while i < n and j < n:
        if numbers[j] >= 2 * numbers[i]: 
            pairs += 1
            i += 1  
        j += 1 

    return pairs

if __name__ == "__main__":
    print(count_pairs([1]))  # 0
    print(count_pairs([1, 2, 3]))  # 1
    print(count_pairs([1, 2, 3, 4]))  # 2
    print(count_pairs([1, 1, 1, 1]))  # 0
    print(count_pairs([10**9, 1, 1, 1]))  # 1
    print(count_pairs([4, 5, 1, 4, 7, 8]))  # 2
    print(count_pairs([1, 2, 3, 2, 4, 6]))  # 3

    numbers = [(x * 999983) % 10**6 + 1 for x in range(10**5)]
    print(count_pairs(numbers))  # 41176
