import time

def dfs(maze, start, end):
    rows = len(maze)
    cols = len(maze[0])

    stack = [(start, [start])]
    visited = set()

    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    steps = 0
    t0 = time.time()

    while stack:
        current, path = stack.pop()
        x, y = current
        steps += 1

        if current == end:
            return path, steps, time.time() - t0

        if current in visited:
            continue

        visited.add(current)

        for dx, dy in directions:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < rows and 0 <= ny < cols:
                if maze[nx][ny] == 0:
                    stack.append(((nx, ny), path + [(nx, ny)]))

    return None, steps, time.time() - t0