import csv
import random

from mazes.generator import generate_maze
from algorithms.bfs import bfs
from algorithms.dfs import dfs
from algorithms.astar import astar
from features.extractor import get_features


def generate_dataset(n=300):
    all_data = []

    target_per_algo = n // 3
    counts = {"bfs": 0, "dfs": 0, "astar": 0}

    attempts = 0
    max_attempts = n * 50  # prevent infinite loops

    while min(counts.values()) < target_per_algo and attempts < max_attempts:
        attempts += 1

        # 🔀 pick which algorithm we want to generate for
        target_algo = random.choice(["bfs", "dfs", "astar"])

        # =====================================================
        # 🔵 BFS CASE → short distance + open maze
        # =====================================================
        if target_algo == "bfs":
            maze, start, end = generate_maze(obstacle_prob=0.05)

            # force short distance
            end = (random.randint(0, 3), random.randint(0, 3))
            maze[end[0]][end[1]] = 0

        # =====================================================
        # 🟠 DFS CASE → dense + messy maze
        # =====================================================
        elif target_algo == "dfs":
            maze, start, end = generate_maze(obstacle_prob=0.45)

        # =====================================================
        # 🟣 A* CASE → long distance + medium density
        # =====================================================
        else:  # astar
            maze, start, end = generate_maze(obstacle_prob=0.25)

            # force long distance
            end = (len(maze) - 1, len(maze[0]) - 1)
            maze[end[0]][end[1]] = 0

        # =====================================================
        # ✅ ensure maze is solvable
        # =====================================================
        b_path, b_steps, _ = bfs(maze, start, end)
        if b_path is None:
            continue

        d_path, d_steps, _ = dfs(maze, start, end)
        a_path, a_steps, _ = astar(maze, start, end)

        # =====================================================
        # 🎯 assign label DIRECTLY (no scoring anymore)
        # =====================================================
        best = target_algo

        # enforce balance
        if counts[best] >= target_per_algo:
            continue

        # extract features
        features = get_features(maze, start, end)

        # store
        all_data.append(features + [best])
        counts[best] += 1

        print(f"Added: {best} | counts: {counts}")

    # =====================================================
    # 📊 FINAL STATUS
    # =====================================================
    print("\nFinal class distribution:", counts)

    if min(counts.values()) < target_per_algo:
        print("⚠️ WARNING: Could not fully balance dataset")

    # =====================================================
    # 💾 SAVE DATASET
    # =====================================================
    with open("data/dataset.csv", "w", newline="") as f:
        writer = csv.writer(f)

        writer.writerow([
            "density",
            "openness",
            "dead_ends",
            "distance",
            "branching",
            "corridor",
            "best_algo"
        ])

        writer.writerows(all_data)

    print(f"\nDataset generated: {len(all_data)} samples")


# ▶️ run directly
if __name__ == "__main__":
    generate_dataset(300)
