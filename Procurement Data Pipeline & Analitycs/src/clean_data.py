import pandas as pd

def clean_data(df):
    df = df.copy()
    df.columns = df.columns.str.strip().str.lower()

    df["supplier_name"] = df["supplier_name"].fillna("Unknown Supplier")
    df["description"] = df["description"].fillna("No Description")
    df["currency"] = df["currency"].fillna("EUR")
    df["country"] = df["country"].fillna("Unknown")

    df["supplier_name"] = df["supplier_name"].astype(str).str.strip()
    df["description"] = df["description"].astype(str).str.strip()
    df["currency"] = df["currency"].astype(str).str.strip()
    df["country"] = df["country"].astype(str).str.strip()

    df["date"] = pd.to_datetime(df["date"], errors="coerce", dayfirst=True)
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
    df["amount"] = df["amount"].fillna(0)
    
    df["currency"] = df["currency"].str.upper()
    df["country"] = df["country"].replace({
        "RO": "Romania",
        "DE": "Germany"
    })
    return df

