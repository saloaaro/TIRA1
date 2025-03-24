def create(n):
    if n < 1:
        return []

    def piiri(n, k):
        if n == 1:
            return [1]
        else:
            circle = list(range(1, n + 1))
            result = []
            index = 0

            while len(circle) > 0:
                index = (index + k - 1) % len(circle)
                result.append(circle.pop(index))

            return result

    return piiri(n, 2)

if __name__ == "__main__":
    print(create(1))  # [1]
    print(create(3))  # [2, 1, 3]
    print(create(7))  # [2, 4, 6, 1, 5, 3, 7]

