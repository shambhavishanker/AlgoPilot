import pandas as pd
from features.extractor import get_features


def predict_best(model, maze, start, end):
    features = get_features(maze, start, end)

    df = pd.DataFrame(
        [features],
        columns=[
    "density",
    "openness",
    "dead_ends",
    "distance",
    "branching",
    "corridor"
     ]
    )

    pred = model.predict(df)[0]

   

    # 🔹 Model already returns strings → keep it simple
    if pred in ["bfs", "dfs", "astar"]:
        algo = pred
    else:
        algo = None

    return algo, features