from collections import deque

def find_components(nodes, edges):
    x = {i: [] for i in nodes}
    for a, b in edges:
        x[a].append(b)
        x[b].append(a)

    y = set()
    z = []

    for i in nodes:
        if i not in y:
            v = []
            q = deque([i])

            while q:
                n = q.popleft()
                if n in y:
                    continue
                y.add(n)
                v.append(n)
                q.extend(x[n])

            z.append(sorted(v))

    return z

if __name__ == "__main__":
    n = [1, 2, 3, 4, 5, 6, 7, 8]
    e = [(1, 2), (1, 3), (2, 3), (4, 5), (4, 6), (5, 7), (6, 7)]
    print(find_components(n, e))  # [[1, 2, 3], [4, 5, 6, 7], [8]]

    n = [1, 2, 3, 4, 5]
    e = []
    print(find_components(n, e))  # [[1], [2], [3], [4], [5]]

    n = [1, 2, 3, 4, 5]
    e = [(1, 2), (1, 3), (1, 4), (1, 5)]
    print(find_components(n, e))  # [[1, 2, 3, 4, 5]]
