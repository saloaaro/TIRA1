class PermutationTracker:
    def __init__(self):
        self.x = set()  
        self.y = 0  
        self.z = None  
        self.v = None  

    def append(self, number):
        self.x.add(number)
        self.y += 1

        if self.y == 1:
            self.z = self.v = number
        else:
            self.z = min(self.z, number)
            self.v = max(self.v, number)

    def check(self):
        if self.y != len(self.x):
            return False
        if self.z != 1 or self.v != self.y:
            return False
        return True


if __name__ == "__main__":
    tracker = PermutationTracker()

    tracker.append(1)
    print(tracker.check()) # True

    tracker.append(4)
    print(tracker.check()) # False

    tracker.append(2)
    print(tracker.check()) # False

    tracker.append(3)
    print(tracker.check()) # True

    tracker.append(2)
    print(tracker.check()) # False

    tracker.append(5)
    print(tracker.check()) # False

    tracker = PermutationTracker()
    total = 0
    for i in range(10**5):
        if i%2 == 0:
            tracker.append(i + 2)
        else:
            tracker.append(i)
        if tracker.check():
            total += 1
    print(total) # 50000