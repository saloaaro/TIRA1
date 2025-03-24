def find(t):
    result = 0
    for num in t:
        result ^= num
    return result

if __name__ == "__main__":
    print(find([2, 1, 3, 2, 3]))  # 1
    print(find([5, 5, 9]))  # 9
    print(find([1, 2, 3, 4, 1, 3, 4]))  # 2
    print(find([8]))  # 8
    print(find([7, 1, 7, 4, 4, 5, 1]))  # 5
