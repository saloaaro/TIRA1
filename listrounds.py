def find_rounds(numbers):
    
    length = len(numbers)
    rounds = []
    target = 1

    while target <= length:
        group = []
        for value in numbers:
            if value == target:
                group.append(value)
                target += 1
        rounds.append(group)

    return rounds

if __name__ == "__main__":
    print(find_rounds([1, 2, 3, 4]))
    # [[1, 2, 3, 4]]

    print(find_rounds([1, 3, 2, 4]))
    # [[1, 2], [3, 4]]    

    print(find_rounds([4, 3, 2, 1]))
    # [[1], [2], [3], [4]]
    
    print(find_rounds([1]))
    # [[1]]

    print(find_rounds([2, 1, 4, 7, 5, 3, 6, 8]))
    # [[1], [2, 3], [4, 5, 6], [7, 8]]
