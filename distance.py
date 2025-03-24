def find(t, k):
    t.sort()
    max_distance = 0
    
    if t[0] != 1:
        max_distance = max(max_distance, t[0] - 1)
    if t[-1] != k:
        max_distance = max(max_distance, k - t[-1])
    
    for i in range(1, len(t)):
        distance = (t[i] - t[i-1]) // 2
        max_distance = max(max_distance, distance)
    
    return max_distance

print(find([1, 2, 9], 11))  # 3
print(find([2, 1, 3], 3))    # 0
print(find([7, 4, 10, 4], 10))  # 3
print(find([15, 2, 6, 4, 18], 20))  # 4
print(find([41222388, 392676742, 307110407, 775934683, 25076911], 809136843))  # 191628970

