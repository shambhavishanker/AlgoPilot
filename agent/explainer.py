def explain_choice(algo, features):
    density, openness, dead_ends, distance, branching, corridor = features

    print("\nWhy this algorithm?")

    if algo == "astar":
        print("- A* is best when goal direction matters")
        print("- It avoids unnecessary exploration")

    elif algo == "bfs":
        print("- BFS guarantees shortest path")
        print("- Good for simple/open mazes")

    elif algo == "dfs":
        print("- DFS explores quickly but not always shortest")
        print("- Works fine for small/simple mazes")

    print("\nQuick summary:")
    print(f"- Walls (density): {round(density, 2)}")
    print(f"- Open space: {round(openness, 2)}")
    print(f"- Dead ends: {round(dead_ends, 2)}")
    print(f"- Start to end distance: {distance}")
