import os
import matplotlib.pyplot as plt

def create_analytics(df):
    os.makedirs("output", exist_ok=True)

    supplier_spend = (
        df.groupby("parent_supplier")["amount"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )
    category_spend = (
        df.groupby("category")["amount"]
        .sum()
        .sort_values(ascending=False)
    )

    monthly_df = df.dropna(subset=["date"]).copy()
    monthly_df["month"] =  monthly_df["date"].dt.to_period("M").astype(str)
    monthly_spend = monthly_df.groupby("month")["amount"].sum().sort_index()

    plt.figure(figsize=(8,5))
    category_spend.plot(kind="bar")
    plt.title("Spending by Category")
    plt.ylabel("Amount")
    plt.tight_layout()
    plt.savefig("output/spend_by_category.png")
    plt.close()

    plt.figure(figsize=(8, 5))
    supplier_spend.plot(kind="bar")
    plt.title("Top Suppliers")
    plt.ylabel("Amount")
    plt.tight_layout()
    plt.savefig("output/top_suppliers.png")
    plt.close()

    plt.figure(figsize=(8,5))
    monthly_spend.plot(kind="line",marker="o")
    plt.title("Spending by month")
    plt.ylabel("Amount")
    plt.tight_layout()
    plt.savefig("output/monthly_spend.png")
    plt.close()

    return category_spend, supplier_spend, monthly_spend
