import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


def train_model():
    # load data
    data = pd.read_csv("data/dataset.csv")

    # features + label
    X = data[[
    "density",
    "openness",
    "dead_ends",
    "distance",
    "branching",
    "corridor"
    ]]
    
    y = data["best_algo"]

    # split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    # model
    model = RandomForestClassifier(n_estimators=100)
    model.fit(X_train, y_train)

    # predictions
    preds = model.predict(X_test)

    # accuracy
    acc = accuracy_score(y_test, preds)

    print(" Model Performance")
    print(f"Accuracy: {round(acc * 100, 2)}%")

    # most common algorithm in dataset
    counts = y.value_counts()
    print("\nMost common best algorithm in data:")
    for algo, count in counts.items():
        print(f"- {algo}: {count} cases")

    # feature importance (clean version)
    print("\nMain factors affecting the decision:")
    for name, score in zip(X.columns, model.feature_importances_):
        print(f"- {name}: {round(score, 2)}")

    return model
