# 🏏 Cricket Performance — Excel Dashboard

An interactive **Excel dashboard** (`nevil_excel_11989_dashborad.xlsx`) analyzing cricket player and team performance, built with PivotTables/summary sheets and chart-ready data feeding a visual Dashboard tab.

---

## 📁 File

| File | Description |
|---|---|
| 📊 `nevil_excel_11989_dashborad.xlsx` | Excel workbook — raw data, cleaned data & interactive dashboard |

---

## 📑 Sheets Overview

| # | Sheet | Size | Description |
|---|---|---|---|
| 1 | 📈 `Dashboard` | 77 rows × 16 cols | 🎯 Main visual dashboard combining all summary tables/charts |
| 2 | 🗃️ `DataSet` | 100 rows × 12 cols | 📥 Raw source data |
| 3 | 🧹 `Clean Data` | 100 rows × 14 cols | ✅ Cleaned data with 2 extra calculated columns |
| 4 | 🌍 `Team Runs` | 9 rows × 3 cols | 🏳️ Total runs scored per team |
| 5 | 🥇 `Top Players` | 11 rows × 2 cols | 🧑‍🎤 Top 10 run-scorers |
| 6 | 🗓️ `Monthly Runs` | 69 rows × 2 cols | 📅 Runs aggregated by month (2015–2024) |

---

## 🧬 Column Details

### 🗃️ DataSet / 🧹 Clean Data
| Column | Description |
|---|---|
| 🗓️ `Date` | Match date |
| 🧑‍🎤 `Player` | Player name |
| 🏳️ `Team` | Player's team |
| ⚔️ `Opponent` | Opposing team |
| 🏃 `Runs` | Runs scored |
| 🎾 `Balls Faced` | Balls faced |
| 4️⃣ `Fours` | Number of fours |
| 6️⃣ `Sixes` | Number of sixes |
| 🎯 `Wickets` | Wickets taken |
| 💰 `Economy Rate` | Bowling economy rate |
| 🏆 `Match Result` | Win / Loss / Tie / No Result |
| 🏟️ `Match Type` | Test / ODI / T20 |
| ⚡ `Strike Rate` | *(Clean Data only)* Calculated batting strike rate |
| 🎯 `Boundary Runs` | *(Clean Data only)* Calculated runs from boundaries |

---

## 📊 Dashboard Highlights

The **Dashboard** sheet brings together 3 summary views side by side:

- 📅 **Runs by Month** (2015–2024) — long-term scoring trend, values ranging from single digits up to 368 in a peak month
- 🥇 **Top 10 Players by Runs** — led by 🧢 **Quinton de Kock (804)**, followed by Steve Smith (717) and KL Rahul (713)
- 🌍 **Runs by Team** — 🏆 **Sri Lanka tops the list (1,334)**, followed by Australia (1,178) and India (1,127)

---

## 🛠️ Tools Used

- 📊 Microsoft Excel
- 🧮 Formulas & calculated columns (Strike Rate, Boundary Runs)
- 📈 Charts / summary tables feeding the Dashboard tab

---

## ▶️ How to Use

1. 📥 Download `nevil_excel_11989_dashborad.xlsx`
2. 📂 Open in Microsoft Excel (or Google Sheets / LibreOffice Calc)
3. 📈 Go to the **Dashboard** tab for the full visual summary
4. 🗃️ Explore `DataSet` and `Clean Data` for the underlying records
5. ✏️ Edit `DataSet` to refresh dependent summary sheets if formulas/links are set to auto-update

---

## ✅ Status

- ✔️ Raw dataset (100 records) included
- ✔️ Cleaned dataset with 2 calculated fields
- ✔️ 3 summary tables: Team Runs, Top Players, Monthly Runs
- ✔️ Combined visual Dashboard tab
- ⚠️ One stray value (`'art'`) found in `Team Runs!C7` — likely a leftover/typo, worth double-checking

---

## 👤 Author

Cricket Performance — Excel Dashboard Project
