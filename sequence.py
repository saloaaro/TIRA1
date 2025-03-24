def generate(n):
    current = 10
    step = 1

    while n > 1:
        current += step
        step += 1
        n -= 1

    return current

if __name__ == "__main__":
    print(generate(1))  # 11
    print(generate(2))  # 22
    print(generate(3))  # 33
    print(generate(10))  # 100
    print(generate(123))  # 505










