import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")


class DataAnalysisVisualizer:
    def __init__(self):
        self.df = None
        self.last_fig = None
        self.last_ax = None

    def run(self):
        while True:
            print("\n======== Data Analysis & Visualization Program ========\n")
            print("Please select an option:")
            print("1. Load Dataset")
            print("2. Explore Data")
            print("3. Perform DataFrame Operations")
            print("4. Handle Missing Data")
            print("5. Generate Descriptive Statistics")
            print("6. Data Visualization")
            print("7. Save Visualization")
            print("8. Exit")

            choice = self._input_int("Enter your choice: ", 1, 8)

            if choice == 1:
                self.load_dataset()
            elif choice == 2:
                self.explore_data()
            elif choice == 3:
                self.df_operations()
            elif choice == 4:
                self.handle_missing_data()
            elif choice == 5:
                self.descriptive_statistics()
            elif choice == 6:
                self.data_visualization()
            elif choice == 7:
                self.save_visualization()
            elif choice == 8:
                print("Exiting the program. Goodbye!")
                break

    def load_dataset(self):
        path = input("\n-- Load Dataset --\nEnter the path of the dataset (CSV file): ").strip()
        if not path:
            print("No path provided.")
            return

        candidates = [path]
        if not path.lower().endswith(".csv"):
            candidates.append(path + ".csv")
        if not os.path.isabs(path):
            candidates.extend([os.path.join(os.getcwd(), p) for p in candidates])

        found = None
        for p in candidates:
            if os.path.isfile(p):
                found = p
                break

        if not found:
            print("File not found. Make sure the path is correct.")
            print("Current working directory:", os.getcwd())
            print("Files here:", os.listdir(os.getcwd()))
            return

        try:
            self.df = pd.read_csv(found)
            if 'transaction_date' in self.df.columns:
                self.df['transaction_date'] = pd.to_datetime(self.df['transaction_date'], errors='coerce')
            if 'amount' in self.df.columns:
                self.df['amount'] = pd.to_numeric(self.df['amount'], errors='coerce')
            print("Dataset loaded successfully!")
            print(f"Rows: {len(self.df)}, Columns: {len(self.df.columns)}")
        except Exception as e:
            print("Failed to load dataset:", type(e).__name__, e)

    def explore_data(self):
        if not self._ensure_df():
            return
        print("\n-- Explore Data --")
        print("1. Display the first 5 rows")
        print("2. Display the last 5 rows")
        print("3. Display column names")
        print("4. Display data types")
        print("5. Display basic info")
        choice = self._input_int("Enter your choice: ", 1, 5)

        if choice == 1:
            print(self.df.head())
        elif choice == 2:
            print(self.df.tail())
        elif choice == 3:
            print(list(self.df.columns))
        elif choice == 4:
            print(self.df.dtypes)
        elif choice == 5:
            self.df.info()

    def df_operations(self):
        if not self._ensure_df():
            return
        print("\n-- Perform DataFrame Operations --")
        print("1. Select columns")
        print("2. Sort by column")
        print("3. Filter rows (simple condition)")
        print("4. Add a new column (expression on existing columns)")
        choice = self._input_int("Enter your choice: ", 1, 4)

        if choice == 1:
            cols = input("Enter column names to select (comma separated): ").split(",")
            cols = [c.strip() for c in cols if c.strip() in self.df.columns]
            if not cols:
                print("No valid columns selected.")
                return
            print(self.df[cols].head())
        elif choice == 2:
            col = input("Enter column to sort by: ").strip()
            if col not in self.df.columns:
                print("Column not found.")
                return
            ascending = input("Ascending? (y/n) [y]: ").strip().lower() != "n"
            print(self.df.sort_values(by=col, ascending=ascending).head())
        elif choice == 3:
            cond = input("Condition: ").strip()
            try:
                filtered = self.df.query(cond)
                print(filtered.head())
            except Exception as e:
                print("Invalid condition:", type(e).__name__, e)
        elif choice == 4:
            name = input("Enter new column name: ").strip()
            expr = input("Enter expression using columns: ").strip()
            if not name or not expr:
                print("Name and expression required.")
                return
            try:
                self.df[name] = self.df.eval(expr)
                print(f"Column '{name}' added successfully.")
                print(self.df[[name]].head())
            except Exception as e:
                print("Failed to add column:", type(e).__name__, e)

    def handle_missing_data(self):
        if not self._ensure_df():
            return
        print("\n-- Handle Missing Data --")
        print("1. Display rows with missing values")
        print("2. Fill missing values with mean (numeric columns)")
        print("3. Drop rows with missing values")
        print("4. Replace missing values with a specific value")
        choice = self._input_int("Enter your choice: ", 1, 4)

        if choice == 1:
            missing = self.df[self.df.isnull().any(axis=1)]
            if missing.empty:
                print("No missing values found in the dataset!")
            else:
                print(missing)
        elif choice == 2:
            numeric_cols = self.df.select_dtypes(include="number").columns
            if len(numeric_cols) == 0:
                print("No numeric columns to fill.")
                return
            self.df[numeric_cols] = self.df[numeric_cols].fillna(self.df[numeric_cols].mean())
            print("Filled numeric columns with mean.")
        elif choice == 3:
            before = len(self.df)
            self.df = self.df.dropna()
            after = len(self.df)
            print(f"Dropped rows with missing values. Rows before: {before}, after: {after}")
        elif choice == 4:
            val = input("Enter the replacement value: ")
            rep = float(val) if self._is_number(val) else val
            self.df = self.df.fillna(rep)
            print("Missing values replaced.")

    def descriptive_statistics(self):
        if not self._ensure_df():
            return
        print("\n-- Generate Descriptive Statistics --")
        print(self.df.describe(include="all"))

    def data_visualization(self):
        if not self._ensure_df():
            return

        print("\n-- Data Visualization --")
        print("1. Bar Plot")
        print("2. Line Plot")
        print("3. Scatter Plot")
        print("4. Pie Chart")

        choice = self._input_int("Enter your choice: ", 1, 4)

        if choice == 1:
            x_col = input("Enter column name for X-axis: ")
            y_col = input("Enter column name for Y-axis: ")

            if x_col not in self.df.columns or y_col not in self.df.columns:
                print("Column name not found in CSV!")
                return

            fig, ax = plt.subplots()
            ax.bar(self.df[x_col], self.df[y_col])
            self._store_and_show(fig, ax)

        elif choice == 2:
            x_col = input("Enter column name for Line Plot: ")

            if x_col not in self.df.columns:
                print("Column name not found in CSV!")
                return

            fig, ax = plt.subplots()
            ax.plot(self.df[x_col])
            ax.set_xlabel("Index")
            ax.set_ylabel(x_col)
            ax.set_title(f"Line Plot of {x_col}")
            self._store_and_show(fig, ax)

        elif choice == 3:
            x_col = input("Enter X-axis column name: ")
            y_col = input("Enter Y-axis column name: ")
            if x_col not in self.df.columns or y_col not in self.df.columns:
                print("Column name not found in CSV!")
                return
            fig, ax = plt.subplots()
            ax.scatter(self.df[x_col], self.df[y_col])
            self._store_and_show(fig, ax)

        elif choice == 4:
            col = input("Enter column name for Pie Chart: ")
            if col not in self.df.columns:
                print("Column not found in CSV!")
                return
            fig, ax = plt.subplots()
            data = self.df[col].value_counts()
            ax.pie(data.values, labels=data.index, autopct='%15.15f%%', startangle=90)
            self._store_and_show(fig, ax)


    def save_visualization(self):
        if self.last_fig is None:
            print("No plot to save. Generate a plot first.")
            return
        filename = input("Enter file name to save the plot: ").strip()
        if not filename:
            print("No filename provided.")
            return
        try:
            self.last_fig.savefig(filename, bbox_inches="tight")
            print(f"Visualization saved as {filename} successfully!")
        except Exception as e:
            print("Failed to save visualization:", type(e).__name__, e)

    def _ensure_df(self):
        if self.df is None:
            print("Please load a dataset first using option 1.")
            return False
        return True

    def _store_and_show(self, fig, ax):
        self.last_fig = fig
        self.last_ax = ax
        plt.show()

    def _input_int(self, prompt, minimum=None, maximum=None):
        while True:
            try:
                v = int(input(prompt))
                if minimum is not None and v < minimum:
                    print("Value too small.")
                    continue
                if maximum is not None and v > maximum:
                    print("Value too large.")
                    continue
                return v
            except ValueError:
                print("Invalid input. Please enter an integer.")

    def _is_number(self, s):
        try:
            float(s)
            return True
        except Exception:
            return False

if __name__ == "__main__":
    try:
        DataAnalysisVisualizer().run()
    except KeyboardInterrupt:
        print("\nInterrupted. Exiting.")
