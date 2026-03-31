from collections import deque
import time

def bfs(maze, start, end):
    rows = len(maze)
    cols = len(maze[0])

    queue = deque()
    queue.append((start, [start]))

    visited = set()
    visited.add(start)

    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    steps = 0
    start_time = time.time()

    while queue:
        (x, y), path = queue.popleft()
        steps += 1

        if (x, y) == end:
            end_time = time.time()
            return path, steps, end_time - start_time

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < rows and 0 <= ny < cols:
                if maze[nx][ny] == 0 and (nx, ny) not in visited:
                    queue.append(((nx, ny), path + [(nx, ny)]))
                    visited.add((nx, ny))

    return None, steps, time.time() - start_time
