import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

class FitnessTracker:
    def __init__(self, filename='fitness_activities.csv'): 
        self.filename = filename 
        self.df = pd.DataFrame()
        
        dir_name = os.path.dirname(self.filename)
        if dir_name:
            os.makedirs(dir_name, exist_ok=True)
        self.load_data()

    def load_data(self):
        if os.path.exists(self.filename):
            try:
                self.df = pd.read_csv(self.filename)
                self.df = self.df.loc[:, ~self.df.columns.str.contains('^Unnamed')]
                if 'Date' in self.df.columns and not self.df.empty:
                    self.df['Date'] = pd.to_datetime(self.df['Date'], errors='coerce')
            except Exception as e:
                print(f"Notice: Starting fresh. (Reason: {e})")
                self.create_empty_df()
        else:
            self.create_empty_df()

    def create_empty_df(self):
        self.df = pd.DataFrame(columns=['Date', 'Activity Type', 'Duration (Minutes)', 'Calories Burned'])

    def log_activity(self, activity_type, duration, calories):
        if duration <= 0 or calories <= 0:
            print("Error: Duration and Calories must be positive numbers.")
            return

        new_data = {
            'Date': pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S'),
            'Activity Type': activity_type,
            'Duration (Minutes)': float(duration),
            'Calories Burned': float(calories)
        }
        
        self.df = pd.concat([self.df, pd.DataFrame([new_data])], ignore_index=True)
        try:
            self.df.to_csv(self.filename, index=False)
            print(f"Successfully logged {activity_type}!")
        except PermissionError:
            print("Error: Close the CSV file in Excel before saving!")

    def calculate_metrics(self):
        if self.df.empty:
            return {"Status": "No data logged yet."}

        metrics = {
            "Total Calories": np.sum(self.df['Calories Burned']),
            "Average Duration": np.mean(self.df['Duration (Minutes)']),
            "Activity Frequency": self.df['Activity Type'].value_counts()
        }
        return metrics

    def show_report(self):
        if self.df.empty:
            print("No data available to plot.")
            return

        plt.figure(figsize=(12, 5))
        
        plt.subplot(1, 2, 1)
        sns.barplot(x='Activity Type', y='Calories Burned', data=self.df, 
                    estimator=np.sum, palette='viridis', hue='Activity Type', legend=False)
        plt.title('Total Calories Burned by Activity')
        plt.xticks(rotation=45)

        plt.subplot(1, 2, 2)
        plt.hist(self.df['Duration (Minutes)'], bins=10, color='skyblue', edgecolor='black')
        plt.title('Distribution of Workout Durations')
        plt.xlabel('Minutes')
        
        plt.tight_layout()
        plt.show()

def main():
    tracker = FitnessTracker()

    while True:
        print("\n--- Fitness Tracker Menu ---")
        print("1. Log Activity")
        print("2. View Metrics")
        print("3. Generate Visual Report")
        print("4. Exit")
        
        choice = input("Enter choice (1-4): ")

        if choice == '1':
            activity = input("Enter activity (e.g., Running, Yoga, Cycling): ")
            try:
                dur = float(input("Enter duration (mins): "))
                cal = float(input("Enter calories burned: "))
                tracker.log_activity(activity, dur, cal)
            except ValueError:
                print("Invalid input. Please enter numbers for duration/calories.")

        elif choice == '2':
            print("\n--- Summary Metrics ---")
            metrics = tracker.calculate_metrics()
            for key, val in metrics.items():
                print(f"{key}:\n{val}\n")

        elif choice == '3':
            tracker.show_report()
        
        elif choice == '4':
            print("Exiting Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-4.")

if __name__ == "__main__":
    main()
