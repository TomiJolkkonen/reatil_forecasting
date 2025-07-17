import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error


def train():
    df = pd.read_csv("data/preprocessed.csv")
    features = ["Store", "Day", "Month", "Year", "Promo"]
    X = df[features]
    y = df["Sales"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    model = XGBRegressor()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print(f"Mean Squared Error: {mse:.2f}")

if __name__ == "__main__":
    train()