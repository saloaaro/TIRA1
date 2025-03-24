def count(t):
    inversiot = 0 

    for i in range(len(t)):
        for j in range(i + 1, len(t)):
            if t[i] > t[j]:  
                inversiot += 1  

    return inversiot

if __name__ == "__main__":
    print(count([1,3,2])) # 1
    print(count([1])) # 0
    print(count([4,3,2,1])) # 6
    print(count([1,8,2,7,3,6,4,5])) # 12