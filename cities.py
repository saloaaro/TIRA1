from collections import defaultdict, deque

class Cities:
    def __init__(self, n):
        self.n = n
        self.graph = defaultdict(list)

    def add_road(self, a, b):
        self.graph[a].append(b)
        self.graph[b].append(a)

    def has_route(self, a, b):
        if a not in self.graph or b not in self.graph:
            return False
        
        visited = set()
        queue = deque([a])

        while queue:
            city = queue.popleft()
            visited.add(city)
            if city == b:
                return True
            for neighbor in self.graph[city]:
                if neighbor not in visited:
                    queue.append(neighbor)

        return False

if __name__ == "__main__":
    c = Cities(5)
    c.add_road(1, 2)
    c.add_road(1, 3)
    c.add_road(4, 5)
    print(c.has_route(1, 5))  # False
    c.add_road(3, 4)
    print(c.has_route(1, 5))  # True
