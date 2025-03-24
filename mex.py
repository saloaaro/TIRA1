class Mex:
    def __init__(self):
        self.data = set()
        self.mex = 0

    def add(self, x):
        self.data.add(x)
        while self.mex in self.data:
            self.mex += 1
        return self.mex

if __name__ == "__main__":
    m = Mex()
    print(m.add(1))  # 0
    print(m.add(3))  # 0
    print(m.add(4))  # 0
    print(m.add(0))  # 2
    print(m.add(5))  # 2
    print(m.add(2))  # 6
