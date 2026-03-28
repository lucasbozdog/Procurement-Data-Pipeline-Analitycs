def standardise_suppliers(df):
    df = df.copy()
    
    supplier_map = {
            "amazon inc.": "Amazon",
            "amazon eu": "Amazon",
            "amazon": "Amazon",
            "staples ltd": "Staples",
            "dhl express": "DHL",
            "microsoft corp": "Microsoft",
            "msft": "Microsoft",
            "meta ads": "Meta",
            "facebook ads": "Meta",
            "ikea": "Ikea",
            "meta" : "Meta",
            "facebook" : "Meta",
            "fedex": "FedEx",
        }
        
    df["supplier_name_clean"] = df["supplier_name"].str.strip().str.lower()
    df["parent_supplier"] = df["supplier_name_clean"].map(supplier_map).fillna(df["supplier_name"])
    return df