def count(t):
    n = len(t)
    count = n  

    for i in range(2, n):
        j = 0
        while i + j < n:
            if (t[i + j] < t[i + j - 1] and t[i + j] < t[i + j - 2]) or (t[i + j] > t[i + j - 1] and t[i + j] > t[i + j - 2]):
                count += 1
                j += 1
            else:
                break

    return count

if __name__ == "__main__":
    print(count([1,2,3,4])) # 7
    print(count([1,4,2,5,3])) # 15
    print(count([7,2,1,3,5,4,6])) # 17
    print(count([1,4,5,2,7,3,6])) # 23


