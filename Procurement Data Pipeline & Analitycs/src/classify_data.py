def classify_spend(df):
    df = df.copy()

    def classify(description):
        text = str(description).lower()

        if any(word in text for word in ["laptop", "monitor", "software", "cloud", "charger"]):
            return "IT"
        elif any(word in text for word in ["paper", "printer", "chairs", "desk", "office"]):
            return "Office"
        elif any(word in text for word in ["shipping", "delivery", "freight"]):
            return "Logistics"
        elif any(word in text for word in ["ads", "campaign", "marketing", "social media"]):
            return "Marketing"
        else:
            return "Other"

    df["category"] = df["description"].apply(classify)

    return df