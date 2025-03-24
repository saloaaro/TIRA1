def count(s, k):
    unique_positions = 1
    visited = set()
    visited.add((0, 0))

    x, y = 0, 0

    for move in s:
        if move == 'U':
            y += 1
        elif move == 'D':
            y -= 1
        elif move == 'L':
            x -= 1
        elif move == 'R':
            x += 1
        position = (x, y)
        if position not in visited:
            unique_positions += 1
            visited.add(position)

    if k % 2 == 0:
        return unique_positions
    else:
        return unique_positions * 2

# Test
print(count("UR", 100))  # 201
print(count("UD", 100))  # 2
print(count("UURRDDL", 500))  # 1506
print(count("L", 10**9))  # 1000000001
print(count("DLUR", 10**9))  # 4

