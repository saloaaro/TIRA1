def count(t):
    n = len(t)
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + t[i]

    count = 0
    sum_set = set()

    for i in range(n):
        for j in range(i, n):
            curr_sum = prefix_sum[j + 1] - prefix_sum[i]
            if curr_sum <= j - i + 1 and curr_sum >= 1 and curr_sum not in sum_set:
                count += 1
                sum_set.add(curr_sum)

    return count


if __name__ == "__main__":
    print(count([1, 1, 1, 1, 1]))  # 4
    print(count([3]))  # 0
    print(count([6, -4]))  # 1
    print(count([5, 4, -2, 1, -3, 2]))  # 4



