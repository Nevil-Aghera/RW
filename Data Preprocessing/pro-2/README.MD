# 🏥 Patient Health Data — Missing Values & Outlier Handling

A data preprocessing project focused on **handling missing values and outliers** in a patient health dataset using **Python, Pandas, Seaborn, and Scikit-learn**. The notebook (`patient_health.ipynb`) walks through detection, imputation, outlier treatment, and final dataset cleanup.

---

## 📁 Project Files

| File | Description |
|---|---|
| 📓 `patient_health.ipynb` | Main Jupyter Notebook — missing value & outlier handling pipeline |
| 📊 `Data/patient_dataset.csv` | ⚠️ Source dataset (referenced in code, **not included** in this upload) |

> ⚠️ **Note:** The notebook loads the dataset with:
> ```python
> df = pd.read_csv('Data\\patient_dataset.csv')
> ```
> Make sure a `Data` folder containing `patient_dataset.csv` sits next to the notebook before running it.

---

## 🧬 Dataset Columns (used in the notebook)

| Column | Description |
|---|---|
| 🎂 `age` | Patient age |
| ⚧️ `gender` | Patient gender |
| ⚖️ `bmi` | Body Mass Index |
| 💓 `blood_pressure` | Blood pressure reading |
| 🩸 `cholesterol` | Cholesterol level |
| 🍬 `glucose` | Glucose level |
| ⚠️ `disease_risk` | Disease risk indicator |

---

## 🔍 What's Inside the Notebook

The notebook is organized into **3 parts**, spanning 40 cells:

### 🧩 Part A — Handling Missing Values
- 🔎 Missing value detection (`isnull().sum()`)
- 📊 Missing values bar plot
- 📈 Missing value percentage summary report + histogram
- 🛠️ Imputation techniques compared:
  - ➕ Mean Imputation
  - 🔁 Most-Frequent (Mode) Imputation — numerical & categorical
  - 🚩 Missing Indicator
  - 🎲 Random Sample Imputation
  - 👥 KNN Imputation
  - 🔄 MICE (Iterative) Imputation

### 📦 Part B — Handling Outliers
- 📐 Z-Score Method (Cholesterol, Glucose)
- 📊 IQR Method (BMI) — Lower/Upper Bound calculation & cleaning
- 📦 Boxplot visualization of cleaned BMI
- 💯 Percentile Method
- ✂️ Winsorization (clipping BMI to 5th–95th percentile)
- ⚖️ Shape & summary statistics comparison (before vs. after)

### ✅ Part C — Final Clean Dataset
- 💾 Export of cleaned datasets: `df_mean.csv`, `df_freq.csv`, `df_final.csv`, `df_imput.csv`, `df_clean_by_Outliers.csv`, `df_clean_bmi.csv`
- 📝 Written report answering:
  - 🏆 Which imputation strategy was most effective?
  - 📉 Outlier handling approach & impact

---

## 🛠️ Tech Stack

- 🐍 Python
- 🐼 Pandas
- 🔢 NumPy
- 📊 Matplotlib
- 🎨 Seaborn
- 🤖 Scikit-learn (`SimpleImputer`, `KNNImputer`, `IterativeImputer`, `MissingIndicator`)

---

## ▶️ How to Run

1. 📥 Clone/download this project folder
2. 📦 Install dependencies:
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn
   ```
3. 📁 Place `patient_dataset.csv` inside a `Data/` folder next to the notebook
4. 📓 Open `patient_health.ipynb` in Jupyter Notebook / JupyterLab / VS Code
5. ▶️ Run all cells in order

---

## ✅ Status

- ✔️ Missing value detection & 5 imputation techniques implemented
- ✔️ Outlier detection via Z-score, IQR & Percentile methods
- ✔️ Winsorization applied
- ✔️ Final cleaned datasets exported
- ⚠️ Source dataset not included — must be supplied separately

---

## 👤 Author

Patient Health Data Cleaning — Missing Values & Outlier Analysis Project
