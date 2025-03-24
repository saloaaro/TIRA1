class QuickList:
    def __init__(self, t):
        self.data = t
        self.n = len(t)
        self.start = 0

    def move(self, k):
        self.start = (self.start + k) % self.n

    def get(self, i):
        index = (self.start + i) % self.n
        return self.data[index]

if __name__ == "__main__":
    q = QuickList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(q.get(4))  # 5
    q.move(3)
    print(q.get(4))  # 8
    q.move(3)
    print(q.get(4))  # 1
    q.move(10)
    print(q.get(4))  # 1
    q.move(7)
    q.move(5)
    print(q.get(0))  # 9
