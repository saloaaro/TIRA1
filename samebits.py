def count(s):
    count_0 = s.count('0')  
    count_1 = s.count('1')  

    if count_0 < count_1:
        return count_0
    else:
        return count_1

if __name__ == "__main__":
    print(count("01101")) # 2
    print(count("1111")) # 0
    print(count("101111")) # 1
    print(count("00001111")) # 4