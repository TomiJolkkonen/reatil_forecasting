import pandas as pd

def preprocess():
    df = pd.read_csv("data/combined.csv")
    df = df[df["Open"] == 1].dropna()
    df["Date"] = pd.to_datetime(df["Date"])
    df["Day"] = df["Date"].dt.day
    df["Month"] = df["Date"].dt.month
    df["Year"] = df["Date"].dt.year
    df.to_csv("data/preprocessed.csv", index=False)

if __name__ == "__main__":
    preprocess()