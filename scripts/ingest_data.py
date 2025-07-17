import pandas as pd

def load_data():
    sales = pd.read_csv("data/train.csv")
    stores = pd.read_csv("data/store.csv")
    df = sales.merge(stores, on="Store")
    df.to_csv("data/combined.csv", index=False)

if __name__ == "__main__":
    load_data()