class MaxList:
    def __init__(self):
        self.m = None

    def append(self, number):
        if self.m is None:
            self.m = number
        self.m = max(self.m, number)

    def max(self):
        return self.m

if __name__ == "__main__":
    numbers = MaxList()

    numbers.append(1)
    numbers.append(2)
    numbers.append(3)
    print(numbers.max()) # 3

    numbers.append(8)
    numbers.append(5)
    print(numbers.max()) # 8

    numbers = MaxList()
    total = 0
    for i in range(10**5):
        numbers.append(i * 999983 % 10**9)
        total += numbers.max()
    print(total) # 99498381797517