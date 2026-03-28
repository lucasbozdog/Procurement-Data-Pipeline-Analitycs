import streamlit as st
import pandas as pd

st.set_page_config(page_title="Procurement Analytics Dashboard", layout="wide")

df = pd.read_csv("data/processed/cleaned_spend_data.csv")

st.title("Procurement Spend Analytics Dashboard")

category_filter = st.multiselect(
    "Filter by category",
    options=sorted(df["category"].dropna().unique()),
    default=sorted(df["category"].dropna().unique())
)

filtered_df = df[df["category"].isin(category_filter)]

total_spend = filtered_df["amount"].sum()
num_suppliers = filtered_df["parent_supplier"].nunique()
top_category = filtered_df.groupby("category")["amount"].sum().idxmax()
avg_transaction = filtered_df["amount"].mean()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Spend", f"{total_spend:.2f}")
col2.metric("Suppliers", num_suppliers)
col3.metric("Top Category", top_category)
col4.metric("Avg Transaction", f"{avg_transaction:.2f}")


st.subheader("Cleaned Data")
st.dataframe(filtered_df)

st.subheader("Spend by Category")
category_spend = (
filtered_df.groupby("category")["amount"]
.sum()
.sort_values(ascending=False)
)
st.bar_chart(category_spend, sort=False)

st.subheader("Top Suppliers")
supplier_spend = (
        filtered_df.groupby("parent_supplier")["amount"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )
st.bar_chart(supplier_spend, sort=False)

st.subheader("Monthly Spend")
if "date" in filtered_df.columns:
    filtered_df["date"] = pd.to_datetime(filtered_df["date"], errors="coerce")
    monthly_df = filtered_df.dropna(subset=["date"]).copy()
    monthly_df["month"] = monthly_df["date"].dt.to_period("M").astype(str)
    monthly_spend = monthly_df.groupby("month")["amount"].sum()
    st.line_chart(monthly_spend)