def show_path(maze, path):
    maze_copy = [row[:] for row in maze]

    for (x, y) in path:
        maze_copy[x][y] = "*"
    for row in maze_copy:
        print(" ".join(str(cell) for cell in row))