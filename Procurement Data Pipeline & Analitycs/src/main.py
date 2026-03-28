import os
from load_data import load_data
from clean_data import clean_data
from transform_data import standardise_suppliers
from classify_data import classify_spend
from analytics import create_analytics

def main():
    file_paths = [
        "data/raw/suppliers_1.csv",
        "data/raw/suppliers_2.csv"
    ]

    df = load_data(file_paths)
    df = clean_data(df)
    df = standardise_suppliers(df)
    df = classify_spend(df)

    os.makedirs("data/processed", exist_ok=True)
    df.to_csv("data/processed/cleaned_spend_data.csv", index=False)

    create_analytics(df)

    print("Pipeline completed successfully.")
    print("Cleaned dataset saved to data/processed/cleaned_spend_data.csv")

if __name__ == "__main__":
    main()
