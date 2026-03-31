import heapq
import time

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])
def astar(maze, start, end):
    rows = len(maze)
    cols = len(maze[0])
    pq = []



    heapq.heappush(pq, (0, start, [start]))
    visited = set()
    cost = {start: 0}
    steps = 0




    t = time.time()
    while pq:
        curr_priority, curr, path = heapq.heappop(pq)
        steps += 1
        if curr == end:
            return path, steps, time.time() - t
        if curr in visited:
            continue
        visited.add(curr)
        x = curr[0]




        y = curr[1]
        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            nx = x + dx
            ny = y + dy
            if nx >= 0 and ny >= 0 and nx < rows and ny < cols:



                
                if maze[nx][ny] == 0:
                    new_cost = cost[curr] + 1
                    if (nx, ny) not in cost or new_cost < cost[(nx, ny)]:
                        cost[(nx, ny)] = new_cost







                        pr = new_cost + heuristic((nx, ny), end)

                        heapq.heappush(pq, (pr, (nx, ny), path + [(nx, ny)]))
    return None, steps, time.time() - t
