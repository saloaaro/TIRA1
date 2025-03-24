def count_rooms(grid):
    h = len(grid)
    w = len(grid[0])

    v = [[False] * w for i in range(h)]
    c = 0

    for y in range(h):
        for x in range(w):
            if grid[y][x] == "." and not v[y][x]:
                c += 1
                explore_room(y, x, grid, v)

    return c

def explore_room(y, x, grid, v):
    s = [(y, x)]
    d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while s:
        cy, cx = s.pop()
        if not (0 <= cy < len(grid) and 0 <= cx < len(grid[0])) or grid[cy][cx] == "#" or v[cy][cx]:
            continue
        
        v[cy][cx] = True
        for dy, dx in d:
            s.append((cy + dy, cx + dx))

if __name__ == "__main__":
    g1 = ["########",
          "#.#..#.#",
          "#####..#",
          "#...#..#",
          "########"]
    print(count_rooms(g1))  # 4

    g2 = ["########",
          "#......#",
          "#.####.#",
          "#......#",
          "########"]
    print(count_rooms(g2))  # 1

    g3 = ["########",
          "######.#",
          "##.#####",
          "########",
          "########"]
    print(count_rooms(g3))  # 2
