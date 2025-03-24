from collections import defaultdict, deque

class Network:
    def __init__(self, n):
        self.n = n
        self.graph = defaultdict(list)

    def add_link(self, a, b):
        self.graph[a].append(b)
        self.graph[b].append(a)

    def best_route(self, a, b):
        if a == b:
            return 0

        if a not in self.graph or b not in self.graph:
            return -1

        visited = set()
        queue = deque([(a, 0)])

        while queue:
            computer, links = queue.popleft()
            visited.add(computer)

            for neighbor in self.graph[computer]:
                if neighbor == b:
                    return links + 1
                if neighbor not in visited:
                    queue.append((neighbor, links + 1))

        return -1

if __name__ == "__main__":
    w = Network(5)
    w.add_link(1, 2)
    w.add_link(2, 3)
    w.add_link(1, 3)
    w.add_link(4, 5)
    print(w.best_route(1, 5))  # -1
    w.add_link(3, 5)
    print(w.best_route(1, 5))  # 2
