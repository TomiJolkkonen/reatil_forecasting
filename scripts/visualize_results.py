import pandas as pd
import matplotlib.pyplot as plt


def visualize():
    df = pd.read_csv("data/preprocessed.csv")
    monthly_sales = df.groupby("Month")["Sales"].mean()

    plt.figure(figsize=(10, 6))
    monthly_sales.plot(kind="bar", color="skyblue")
    plt.title("Keskimääräinen kuukausimyynti")
    plt.xlabel("Kuukausi")
    plt.ylabel("Myynti")
    plt.tight_layout()
    plt.savefig("plots/monthly_sales.png")
    plt.show()

if __name__ == "__main__":
    visualize()