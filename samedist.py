def find(t):
    first_seen = {}  
    max_distance = 0  

    for i, num in enumerate(t):
        if num not in first_seen:
            first_seen[num] = i

    for i, num in enumerate(t):
        if num in first_seen:
            distance = i - first_seen[num]
            max_distance = max(max_distance, distance)

    for i, num in enumerate(t):
        if num in first_seen:
            max_distance = max(max_distance, i - first_seen[num])

    return max_distance

if __name__ == "__main__":
    print(find([1, 2, 1, 1, 2]))  # 3
    print(find([1, 2, 3, 4]))  # 0
    print(find([1, 1, 1, 1, 1]))  # 4
    print(find([1, 1, 2, 3, 4]))  # 1
    print(find([1, 5, 1, 5, 1]))  # 4







