def solve(t, x):
    t.sort()
    
    count = 0
    total_weight = 0
    
    for weight in t:
        if total_weight + weight <= x:
            total_weight += weight
            count += 1
        else:
            break
    
    return count

if __name__ == "__main__":
    print(solve([1, 1, 1, 1], 2))  # 2
    print(solve([2, 5, 3, 2, 8, 7], 10))  # 3
    print(solve([2, 3, 4, 5], 1))  # 0
    print(solve([2, 3, 4, 5], 10**9))  # 4
    print(solve([10**9, 1, 10**9], 10**6))  # 1

