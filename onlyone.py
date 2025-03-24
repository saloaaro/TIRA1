def find(t):
    count = {}
    
    for num in t:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    
    for num in count:
        if count[num] == 1:
            return num

if __name__ == "__main__":
    print(find([1,1,2,1]))  # 2
    print(find([4,5,5]))  # 4
    print(find([1,1,1,1,2]))  # 2
    print(find([8,8,5,8,8]))  # 5





