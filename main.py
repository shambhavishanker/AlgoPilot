import random

from mazes.generator import generate_maze
from algorithms.bfs import bfs
from algorithms.dfs import dfs
from algorithms.astar import astar

from utils.helpers import get_user_maze
from utils.visualization import show_path

from ml.train import train_model
from ml.predict import predict_best

from agent.explainer import explain_choice


def print_maze(maze):
    for row in maze:
        print(" ".join(str(cell) for cell in row))


def main():

    print("Choose option:")
    print("1. Generate random maze")
    print("2. Enter your own maze")
    print("3. Exit")

    choice = input("Enter choice: ")

    
    if choice == "1":

        mode = random.choice(["bfs", "dfs", "astar"])
        

        if mode == "bfs":
            maze, start, end = generate_maze(obstacle_prob=0.05)
            end = (random.randint(0, 3), random.randint(0, 3))
            maze[end[0]][end[1]] = 0

        elif mode == "dfs":
            maze, start, end = generate_maze(obstacle_prob=0.45)

        else:  # astar
            maze, start, end = generate_maze(obstacle_prob=0.25)
            end = (len(maze) - 1, len(maze[0]) - 1)
            maze[end[0]][end[1]] = 0

   
    elif choice == "2":
        maze, start, end = get_user_maze()

    elif choice == "3":
        print("Exiting...")
        return

    else:
        print("Invalid choice, using smart random mode")
        maze, start, end = generate_maze()

   
    print("\nMaze:")
    print_maze(maze)

    print(f"\nStart: {start}")
    print(f"End: {end}")

    
    bfs_path, bfs_steps, bfs_time = bfs(maze, start, end)
    dfs_path, dfs_steps, dfs_time = dfs(maze, start, end)
    astar_path, astar_steps, astar_time = astar(maze, start, end)

    print("\nAlgorithm Comparison")
    print(f"BFS  -> Steps: {bfs_steps}, Time: {bfs_time:.5f}")
    print(f"DFS  -> Steps: {dfs_steps}, Time: {dfs_time:.5f}")
    print(f"A*   -> Steps: {astar_steps}, Time: {astar_time:.5f}")

   
    model = train_model()

    
    best_algo, features = predict_best(model, maze, start, end)

    
    if best_algo not in ["bfs", "dfs", "astar"]:
        print("No valid prediction, defaulting to A*")
        best_algo = "astar"

    print(f"\nPredicted best algorithm: {best_algo}")

    
    explain_choice(best_algo, features)

    
    if best_algo == "bfs":
        path = bfs_path
    elif best_algo == "dfs":
        path = dfs_path
    else:
        path = astar_path

    
    if path is None:
        print("\nno valid path found in this maze.")
    else:
        print("\nPath Visualization")
        show_path(maze, path)


if __name__ == "__main__":
    main()