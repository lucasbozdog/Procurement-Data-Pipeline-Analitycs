# 📊 Procurement Data Pipeline & Analytics

A simple end-to-end data pipeline that simulates real-world procurement data processing.
The project demonstrates how messy supplier data can be cleaned, standardized, categorized, and transformed into actionable insights.

---

## 🚀 Project Overview

This project replicates a simplified version of what companies like Sievo do:

* Load raw procurement data from multiple sources
* Clean and standardize inconsistent data
* Group suppliers under parent companies
* Classify spend into categories
* Generate analytics and visual insights

---

## 🧱 Project Structure

```
project/
│
├── data/
│   ├── raw/
│   │   ├── suppliers_1.csv
│   │   ├── suppliers_2.csv
│   ├── processed/
│   │   └── cleaned_spend_data.csv
│
├── output/
│   ├── category_spend.png
│   ├── supplier_spend.png
│   ├── monthly_spend.png
│
├── src/
│   ├── load_data.py
│   ├── clean_data.py
│   ├── transform_data.py
│   ├── classify_data.py
│   ├── analytics.py
│   └── main.py
│
├── app.py
└── README.md
```
---

## ⚙️ Pipeline Steps

### 1. 📥 Data Loading (`load_data.py`)

* Reads multiple CSV files
* Combines them into a single dataset

---

### 2. 🧹 Data Cleaning (`clean_data.py`)

* Handles missing values
* Standardizes text (lowercase, trimming spaces)
* Converts:

  * dates → datetime
  * amounts → numeric
* Normalizes country and currency formats

---

### 3. 🏢 Supplier Standardization (`transform_data.py`)

* Maps different supplier names to a parent supplier

Example:

```
Amazon Inc. → Amazon
Amazon EU → Amazon
```

---

### 4. 🧠 Spend Classification (`classify_data.py`)

* Categorizes transactions based on keywords in descriptions

Categories include:

* IT
* Office
* Logistics
* Marketing
* Other

---

### 5. 📊 Analytics (`analytics.py`)

Generates insights using grouped data:

* Spend by category
* Top suppliers by spend
* Monthly spending trends

Outputs:

* Bar charts
* Line chart for monthly spend

---

### 6. 🌐 Interactive Dashboard (`app.py` - Streamlit)

Provides an interactive interface to explore the data:

- Filter data by category  
- View cleaned dataset  
- Visualize:
  - Spending by category  
  - Top suppliers (sorted descending)  
  - Monthly spending trends  

---

## ▶️ How to Run

### 1. Install dependencies

```
pip install pandas matplotlib streamlit
```

---

### 2. Run the pipeline

```
python src/main.py
```

After running this, the file will be updated:
data/processed/cleaned_spend_data.csv

⚠️ If you make changes to the pipeline or raw data, you must run this step again before using Streamlit.


---
### 3. Run the Streamlit dashboard

```
python -m streamlit run app.py
```
This will open an interactive dashboard in your browser.

---

## 📂 Output

After running the pipeline, the following files will be generated:

* Clean dataset:

```
data/processed/cleaned_spend_data.csv
```

* Charts:

```
output/
├── monthly_spend.png
├── spend_by_category.png
└── top_suppliers.png
```

---

## 📌 Example Insights

* Identify top suppliers by total spend  
* Track spending trends over time  
* Analyze spending distribution across categories  
* Interactively explore data using filters (Streamlit dashboard)  

---

## 💡 Key Concepts Demonstrated

* Data cleaning and preprocessing  
* Handling real-world messy data  
* Data transformation and normalization  
* Feature engineering (categorization)  
* Aggregation and analytics using pandas  
* Building interactive dashboards with Streamlit  

---

## 🎯 Why This Project

This project was built to simulate real-world data engineering and procurement analytics workflows, focusing on:

* Structured data pipelines  
* Business-relevant transformations  
* Clear and explainable analytics  
* Connecting backend data processing with frontend visualization  

---

## 🔧 Future Improvements

* Implement currency conversion  
* Use a database instead of CSV files  
* Add more advanced filters and KPIs in the dashboard  

---

## 👤 Author

Luca Bozdog
Computer Science Student

---
