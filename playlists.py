def count(t):
    n = len(t)  
    seen = {}   
    start = 0   
    count = 0   

    for end in range(n):
        song = t[end]
        if song in seen and seen[song] >= start:
            start = seen[song] + 1
        seen[song] = end
        count += end - start + 1

    return count

if __name__ == "__main__":
    print(count([1,2,3,4]))  # 10
    print(count([1,1,1,1]))  # 4
    print(count([5]))        # 1
    print(count([1,3,2,3,4,2,4,1,2,1]))  # 24











