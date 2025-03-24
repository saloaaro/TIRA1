def count(a, b, c):
    max_candies_a = c // a
    max_candies_b = c // b 
    return max(max_candies_a, max_candies_b)

if __name__ == "__main__":
    print(count(3, 4, 11)) # 3
    print(count(5, 1, 100)) # 100
    print(count(2, 3, 1)) # 0
    print(count(2, 3, 9)) # 4