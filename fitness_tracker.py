# importing all necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Creating class
class FitnessTracker:
    def __init__(self, file="fitness_activities.csv"):
        self.file = file
        self.df = pd.read_csv(self.file)
        print("CSV loaded!")
    def log_activity(self):
            print("\nLog activites: ")
            activity_type = input("Enter Activity Type: ")
            
            duration = float(input("Enter Duration in (minutes): "))
            if duration <= 0:
                print("Error! Please enter a valid number")
                return
                
            calories = float(input("Enter Calories Burned: "))
            if calories <= 0:
                print("Error! Please enter a valid number")
                return
                
            date = input("Enter Date (YYYY-MM-DD): ")
    
            new_row = {'Date': date,
                'Activity Type': activity_type,
                'Duration (Minutes)': int(duration),
                'Calories Burned': int(calories)}
            
            self.df = pd.concat([self.df, pd.DataFrame([new_row])], ignore_index=True)
            self.df.to_csv(self.file, index=False)
            print(f"'{activity_type}' added activity.")
                    
        
    def calculate_metrics(self):
        if self.df.empty:
            print("No CSV found. Please Try again!")
            return
        total_calories = np.sum(self.df['Calories Burned'])
        avg_duration = np.mean(self.df['Duration (Minutes)'])
        
        print("\nHealth Details:")
        print("Total Calories Burned:", total_calories)
        print("Average Duration (Mins):",avg_duration)
        
        # additional metrics: 
        self.df['Calories per Minute'] = self.df['Calories Burned'] / self.df['Duration (Minutes)']
        
    # filter activities:
    def filter_activities(self, activity_name):
            filtered_data = self.df[self.df['Activity Type'].str.lower() == activity_name.lower()]
            return filtered_data
    
    # visualization 
    def visualize(self):
            plt.figure(figsize=(10, 7))
            plt.subplot(2, 2, 1)
            sns.barplot(x='Activity Type', y='Duration (Minutes)', data=self.df)
            plt.title('Time Spent on Activity')
            plt.subplot(2, 2, 2)
            plt.plot(self.df['Date'], self.df['Calories Burned'], marker='o')
            plt.title('Calories Burned Over Time')   
            plt.subplot(2, 2, 3)
            activity_counts = self.df['Activity Type'].value_counts()
            plt.pie(activity_counts, labels=activity_counts.index, autopct='%1.1f%%')
            plt.title('Activity Distribution')
            plt.subplot(2, 2, 4)
            sns.heatmap(self.df[['Duration (Minutes)', 'Calories Burned']].corr(), annot=True, cmap='coolwarm')
            plt.title('Correlation b/w duration & calories')
            plt.tight_layout()
            plt.show()
    
    # generating report:
    def generate_report(self):
            print("\nfitness tracker report:")
            print("Total Activities:", len(self.df))
            self.calculate_metrics()
            
t = FitnessTracker('fitness_activities.csv')
while True:
    print("\nPersonal Fitness Tracker:")
    print("1. Add New Activity")
    print("2. View Summary Report & Metrics")
    print("3. Filter Activities")
    print("4. Visualization")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    match choice:
        case "1":
            t.log_activity()
        case "2":
            t.generate_report()
        case "3":
            user = input("Enter Activity Type to filter: ")
            r = t.filter_activities(user)
            if r.empty:
                print(f"No records found for '{user}'.")
            else:
                print("Filtered Activities:")
                print(r)
        case "4":
            t.visualize()
        case "5":
            print("Exiting from personal tracker!")
            break
        case _:
            print("Invalid choice. Try again.")
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
       
       
       
       
       
       
       
       
       
       
       
   
