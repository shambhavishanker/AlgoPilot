def get_features(maze, start, end):
    rows = len(maze)
    cols = len(maze[0])
    total_cells = rows * cols
    walls = 0
    open_cells = 0
    dead_ends = 0
    branching_total = 0
    corridor_cells = 0
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    for i in range(rows):
        for j in range(cols):
            if maze[i][j] == 1:
                walls += 1
                continue
            open_cells += 1
            neighbors = 0
            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                if 0 <= ni < rows and 0 <= nj < cols:
                    if maze[ni][nj] == 0:
                        neighbors += 1
            branching_total += neighbors
            if neighbors == 1:
                dead_ends += 1
            if neighbors == 2:
                corridor_cells += 1
    density = walls / total_cells
    openness = open_cells / total_cells
    dead_ratio = dead_ends / (open_cells + 1)
    branching_factor = branching_total / (open_cells + 1)
    corridor_ratio = corridor_cells / (open_cells + 1)
    distance = abs(start[0] - end[0]) + abs(start[1] - end[1])
    return [
        density,
        openness,
        dead_ratio,
        distance,
        branching_factor,
        corridor_ratio
    ]