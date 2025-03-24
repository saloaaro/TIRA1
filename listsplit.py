def count(t):
    n = len(t)
    left_mins = [0] * n
    right_mins = [0] * n
    min_count = {}  
    result = 0

    min_val = float('inf')
    for i in range(n):
        min_val = min(min_val, t[i])
        left_mins[i] = min_val

    min_val = float('inf')
    for i in range(n - 1, -1, -1):
        min_val = min(min_val, t[i])
        right_mins[i] = min_val

    for i in range(n - 1):
        if left_mins[i] == right_mins[i + 1]:
            result += 1

    return result

if __name__ == "__main__":
    print(count([2, 1, 1, 3]))  # 1
    print(count([1, 1, 1, 1]))  # 3
    print(count([1, 2, 3, 1, 2, 3]))  # 3
    print(count([1, 2, 3, 4, 3, 2, 1]))  # 6
    print(count([4, 3, 2, 1, 2, 3, 4]))  # 0

