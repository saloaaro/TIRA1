class RepeatList:
    def __init__(self):
        self.x = False
        self.y = set()

    def append(self, number):
        if number in self.y:
            self.x = True
        self.y.add(number)

    def repeat(self):
        return self.x

if __name__ == "__main__":
    numbers = RepeatList()

    print(numbers.repeat()) # False

    numbers.append(1)
    numbers.append(2)
    numbers.append(3)
    print(numbers.repeat()) # False

    numbers.append(2)
    print(numbers.repeat()) # True

    numbers.append(5)
    print(numbers.repeat()) # True

    numbers = RepeatList()
    total = 0
    for i in range(10**5):
        numbers.append(i * 999983 % 12345)
        if numbers.repeat():
            total += 1
    print(total) # 87655
