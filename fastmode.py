class FastMode:
    def __init__(self):
        self.data = {}
        self.max_count = 0
        self.mode_value = None

    def add(self, x, k):
        if x in self.data:
            self.data[x] += k
        else:
            self.data[x] = k

        if self.data[x] > self.max_count:
            self.max_count = self.data[x]
            self.mode_value = x
        elif self.data[x] == self.max_count and x < self.mode_value:
            self.mode_value = x

    def mode(self):
        return self.mode_value

if __name__ == "__main__":
    m = FastMode()
    m.add(4, 7)
    print(m.mode())  # 4
    m.add(8, 5)
    print(m.mode())  # 4
    m.add(8, 3)
    print(m.mode())  # 8
    m.add(4, 1)
    print(m.mode())  # 4
