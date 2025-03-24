def count(t):
    t_set = set(t)
    max_count = 0

    for num in t_set:
        if num - 1 not in t_set:
            current_num = num
            current_count = 1

            while current_num + 1 in t_set:
                current_num += 1
                current_count += 1

            max_count = max(max_count, current_count)

    return max_count

if __name__ == "__main__":
    print(count([1, 1, 1, 1]))  # 1
    print(count([10, 4, 8]))  # 1
    print(count([7, 6, 1, 8]))  # 3
    print(count([1, 2, 1, 2, 1, 2]))  # 2
    print(count([987654, 12345678, 987653, 999999, 987655]))  # 3


