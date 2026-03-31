import random
from algorithms.bfs import bfs  # used to ensure maze is solvable


def generate_maze(rows=10, cols=10, obstacle_prob=0.2):
    """
    Generates a random maze that is GUARANTEED to be solvable.
    
    0 = open path
    1 = wall
    """

    while True:  # 🔥 keep trying until we get a solvable maze

        maze = []

        # 🔹 generate random grid
        for i in range(rows):
            row = []
            for j in range(cols):
                if random.random() < obstacle_prob:
                    row.append(1)  # wall
                else:
                    row.append(0)  # path
            maze.append(row)

        # 🔹 define start & end
        start = (0, 0)
        end = (rows - 1, cols - 1)

        # 🔹 ensure start and end are NOT blocked
        maze[start[0]][start[1]] = 0
        maze[end[0]][end[1]] = 0

        # 🔹 check if path exists using BFS
        path, _, _ = bfs(maze, start, end)

        if path is not None:
            return maze, start, end