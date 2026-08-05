# 💳 Customer Credit Risk — End-to-End Data Science Pipeline

A complete data science workflow covering **conceptual foundations, data acquisition, cleaning, feature engineering, scaling, and transformation** on a customer credit risk dataset. Built with **Python, Pandas, Scikit-learn, SciPy, and ydata-profiling**.

---

## 📁 Project Files

| File | Description |
|---|---|
| 📓 `customer_credit.ipynb` | Main Jupyter Notebook — full end-to-end pipeline |
| 📊 `customer_credit_risk_dataset.csv` | ⚠️ Source dataset (referenced in code, **not included** in this upload) |
| 🗄️ `customer_credit_risk_dataset.db` | SQLite DB generated from the CSV during the pipeline |
| 📁 `Data/cleaned_credit_risk_dataset.csv` | ⚠️ Final cleaned dataset (referenced, **not included**) |

> ⚠️ **Note:** Place `customer_credit_risk_dataset.csv` in the notebook's root folder, and `cleaned_credit_risk_dataset.csv` inside a `Data/` subfolder, before running.

---

## 🔍 What's Inside the Notebook

The notebook is organized into **8 parts (A–H)** across 81 cells:

### 🧠 Part A — Conceptual Foundation
- 📝 Short notes: What is Data Analysis? How to Plan a Data Science Project? How to Frame an ML Problem?
- 🔢 Tensors explained in-depth with NumPy examples

### 🌐 Part B — Data Acquisition
- 📄 Load data from **CSV**
- 🧾 Parse **JSON** (generated sample customer metadata)
- 🗄️ Fetch/store records via **SQL** (SQLite)
- 🔌 Pull data from a **REST API** (`randomuser.me`)

### 🔎 Part C — Data Understanding & Cleaning
- ℹ️ Explore with `.info()` and `.describe()`
- 📊 **Pandas Profiling** (`ydata-profiling`) data quality report
- 🛠️ Missing data handling (6 techniques):
  - ➕ Simple Imputer — mean (numeric)
  - 🔁 Simple Imputer — most frequent (categorical)
  - 🏷️ Most Frequent Category Imputation
  - 🚩 Missing Indicator + Random Sample Imputation
  - 👥 KNN Imputer
  - 🔄 MICE (Iterative Imputer)
  - ✂️ Complete Case Analysis (drop rows)

### 📦 Part D — Outlier Handling
- 📐 Z-Score Method
- 📊 IQR Method
- 💯 Percentile Method
- 🎯 Winsorization

### 🏗️ Part E — Feature Engineering
- 🔀 Mixed variable type handling (numeric + categorical)
- 🗓️ Date/Time feature extraction (Year, Month, Day, Weekday)
- 🔢 Encoding categorical variables: **Ordinal**, **Label**, **One-Hot**
- 📊 Encoding numerical features: **Binning**, **Binarization**, **Quantile Binning**, **K-Means Binning**

### ⚖️ Part F — Feature Scaling
- 📏 Standardization (Z-score)
- 🧮 Normalization
- 📉 Min-Max Scaling
- 🔢 MaxAbs Scaling
- 🛡️ Robust Scaling

### 🔧 Part G — Feature Construction & Transformation
- 📈 FunctionTransformer: log, reciprocal, square root
- 🔁 PowerTransformer: Box-Cox & Yeo-Johnson
- 🧩 ColumnTransformer for mixed-column pipelines
- 🆕 Engineered features:
  - 💰 Debt-to-Income Ratio
  - 📆 Average Monthly Transactions
  - 💸 Spending-to-Income Ratio

### 🏁 Part H — Final Deliverable
- ✅ Final cleaned & transformed dataset (300 rows × 34 columns, 0 missing values)
- 📝 Written report covering:
  - 🩹 Missing value strategy effectiveness
  - 📉 Outlier handling results (0 outliers detected — synthetic, tightly-bounded data)
  - 🔠 Encoding methods applied & rationale
  - ⚖️ Scaling/transformation choices & rationale
  - 🧬 Engineered features & their usefulness
  - 🎯 Final dataset readiness for ML modeling (target: `default_flag`)

---

## 🛠️ Tech Stack

- 🐍 Python
- 🐼 Pandas & 🔢 NumPy
- 📊 SciPy (`stats`, `winsorize`)
- 🤖 Scikit-learn (imputers, encoders, scalers, transformers)
- 📈 ydata-profiling (Pandas Profiling)
- 🗄️ SQLite3
- 🌐 Requests (API calls)

---

## ▶️ How to Run

1. 📥 Clone/download this project folder
2. 📦 Install dependencies:
   ```bash
   pip install pandas numpy scipy scikit-learn requests ydata-profiling
   ```
3. 📁 Place `customer_credit_risk_dataset.csv` in the notebook's root folder, and `cleaned_credit_risk_dataset.csv` inside `Data/`
4. 📓 Open `customer_credit.ipynb` in Jupyter Notebook / JupyterLab / VS Code
5. ▶️ Run all cells in order

---

## ✅ Status

- ✔️ Full pipeline implemented: acquisition → cleaning → feature engineering → scaling → transformation
- ✔️ 6 missing-value imputation techniques compared
- ✔️ 4 outlier detection/treatment methods applied
- ✔️ Multiple encoding & scaling strategies used
- ✔️ 3 new domain-relevant features engineered
- ✔️ Final dataset ready for ML modeling (0 missing values, fully numeric)
- ⚠️ Source & cleaned CSV files not included — must be supplied separately
