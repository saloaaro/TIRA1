def count(r):
    num_rooms = 0
    visited = set()

    for i in range(len(r)):
        for j in range(len(r[0])):
            if r[i][j] == '.' and (i, j) not in visited:
                dfs(r, i, j, visited)
                num_rooms += 1

    return num_rooms

def dfs(r, i, j, visited):
    if i < 0 or i >= len(r) or j < 0 or j >= len(r[0]) or r[i][j] == '#' or (i, j) in visited:
        return

    visited.add((i, j))

    for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        dfs(r, i + x, j + y, visited)

if __name__ == "__main__":
    r = ["########",
         "#..#...#",
         "####.#.#",
         "#..#.#.#",
         "########"]
    print(count(r)) # 3
