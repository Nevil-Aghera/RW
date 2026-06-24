# 📊 Data Profiler Project

## 🚀 Project Overview

The **Data Profiler Project** demonstrates the complete Data Science workflow, including **Data Acquisition**, **Data Cleaning**, **Exploratory Data Analysis (EDA)**, **Visualization**, and **Automated Profiling**.

The project utilizes powerful Python libraries such as **Pandas**, **NumPy**, **Matplotlib**, **Seaborn**, **SQLite**, **Requests**, and **YData Profiling** to analyze and understand datasets from multiple sources.

🎯 **Objective:** Collect data from different sources, preprocess it, perform exploratory analysis, create visualizations, and generate automated profiling reports for better decision-making.

---

## 🎯 Objectives

✅ Import datasets from multiple sources

✅ Parse JSON data

✅ Connect to SQL databases and fetch records

✅ Retrieve data from APIs

✅ Clean and preprocess data

✅ Perform Exploratory Data Analysis (EDA)

✅ Generate automated profiling reports

✅ Prepare datasets for Machine Learning applications

---

## 🛠️ Technologies Used

| Technology          | Purpose                   |
| ------------------- | ------------------------- |
| 🐍 Python           | Programming Language      |
| 📓 Jupyter Notebook | Development Environment   |
| 🐼 Pandas           | Data Manipulation         |
| 🔢 NumPy            | Numerical Computing       |
| 📈 Matplotlib       | Data Visualization        |
| 📊 Seaborn          | Statistical Visualization |
| 🗄️ SQLite3         | Database Management       |
| 🌐 Requests         | API Integration           |
| 📋 YData Profiling  | Automated Data Profiling  |

---

## 📂 Project Structure

```text
DataProfiler/
│
├── 📓 Data_Profiler.ipynb
├── 📄 student_performance_4000.csv
├── 📄 students.json
├── 🗄️ students.db
├── 📊 profiling_report.html
├── 📖 README.md
└── 📦 requirements.txt
```

---

## 📥 Data Acquisition

### 📄 Load CSV File

```python
import pandas as pd

df = pd.read_csv("student_performance_4000.csv")
```

### 📄 Parse JSON File

```python
df_json = pd.read_json("students.json")
```

### 🗄️ Connect to SQL Database

```python
import sqlite3

conn = sqlite3.connect("students.db")
df_sql = pd.read_sql("SELECT * FROM students", conn)
```

### 🌐 Fetch Data from API

```python
import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")
data = response.json()
```

---

## 🔍 Data Understanding

The following functions were used for initial exploration:

```python
df.head()
df.info()
df.describe()
```

### 🔎 Data Quality Checks

```python
df.isnull().sum()
df.duplicated().sum()
```

---

## 🧹 Data Cleaning

The following preprocessing operations were performed:

* ✅ Handle Missing Values
* ✅ Remove Duplicate Records
* ✅ Correct Data Types
* ✅ Remove Irrelevant Columns

Example:

```python
df.fillna(df.mean(numeric_only=True), inplace=True)
df.drop_duplicates(inplace=True)
```

---

## 📈 Exploratory Data Analysis (EDA)

### 📊 Univariate Analysis

* Histogram
* Boxplot
* Countplot

### 🔗 Bivariate Analysis

* Scatter Plot
* Correlation Analysis
* Bar Charts

### 🌐 Multivariate Analysis

* Pair Plot
* Heatmap
* Correlation Matrix

---

## 🤖 Automated Profiling

Generate a comprehensive profiling report using **YData Profiling**.

```python
from ydata_profiling import ProfileReport

profile = ProfileReport(df)

profile.to_file("profiling_report.html")
```

📋 The report includes:

* Missing Values Analysis
* Correlation Analysis
* Data Type Summary
* Statistical Overview
* Duplicate Detection
* Outlier Detection

-----


## 🏁 Conclusion

This project successfully demonstrates the end-to-end Data Science process, from **Data Acquisition** and **Data Cleaning** to **EDA**, **Visualization**, and **Automated Profiling**.

The final cleaned dataset and profiling report provide meaningful insights and establish a strong foundation for future **Machine Learning** and **Data Analytics** projects.

---
