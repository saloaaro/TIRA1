from collections import deque

def connected(nodes, edges):
    if not nodes:
        return True 
    
    x = {i: [] for i in nodes}
    for a, b in edges:
        x[a].append(b)
        x[b].append(a)

    y = set()
    z = deque([nodes[0]])

    while z:
        n = z.popleft()
        if n in y:
            continue
        y.add(n)
        z.extend(x[n])

    return len(y) == len(nodes)

if __name__ == "__main__":
    n = [1, 2, 3, 4, 5]
    e = [(1, 2), (1, 3), (1, 4), (2, 4), (2, 5), (3, 4), (4, 5)]
    print(connected(n, e))  # True

    n = [1, 2, 3, 4, 5, 6, 7, 8]
    e = [(1, 2), (1, 3), (2, 3), (4, 5), (4, 6), (5, 7), (6, 7)]
    print(connected(n, e))  # False

    n = [1, 2, 3, 4, 5]
    e = []
    print(connected(n, e))  # False

    n = [1, 2, 3, 4, 5]
    e = [(1, 2), (1, 3), (1, 4), (1, 5)]
    print(connected(n, e))  # True
