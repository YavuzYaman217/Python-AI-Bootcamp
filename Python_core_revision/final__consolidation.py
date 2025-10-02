# Import necessary libraries: pandas for data manipulation and numpy for numerical operations.
import pandas as pd
import numpy as np

# --- Data Creation ---
# Create a DataFrame for employee information.
df_employees = pd.DataFrame({
    'EmpID': [1, 2, 3, 4, 5, 6],
    'Name': ['Ayşe Yılmaz', 'Burak Can', 'Ceren Ak', 'Deniz Su', 'Emre Kaya', 'Furkan Tek'],
    'DeptID': [10, 20, 10, 30, 20, 30],
    'Salary': [65000, 85000, 72000, 58000, 95000, 60000]
})

# Create a DataFrame for employee performance reviews, including missing values (np.nan).
df_reviews = pd.DataFrame({
    'EmpID': [1, 2, 3, 4, 5, 7],  # Note: EmpID 7 does not exist in df_employees.
    'Score': [7, 11, 0, np.nan, 8, 5], 
    'Projects': [4, 5, 2, np.nan, 3, 1] 
})

# --- Decorator for Data Validation ---
# Define a decorator to check if a performance score is valid before processing.
def check_score(func):
    # The wrapper function receives the arguments of the decorated function.
    def wrapper(*args,**kwargs):
        # Get the 'score' from keyword arguments.
        score = kwargs.get('score', None)
        # If the score is greater than 10, it's considered invalid.
        if score is not None and score > 10:
            print(f"Score {score} is invalid and cannot be greater than 10. Setting Risk Index to NaN.")
            return np.nan # Return NaN for invalid scores.
        # If the score is valid, call the original function.
        return func(*args,**kwargs)
    return wrapper

# --- Performance Calculation Function ---
# Apply the decorator to the function that calculates the performance status.
@check_score
def get_performance_status(score, projects):
    # If the score is missing (NaN), return a default high risk value (e.g., 50.0).
    if pd.isna(score):
        return 50.0
    
    # If the score is zero, it indicates a critical issue, return a very high risk value (e.g., 100.0).
    if score == 0:
        return 100.0
    
    # If the number of projects is missing, it might indicate no project data, return 0.0 risk.
    if pd.isna(projects):
        return 0.0
    
    # Calculate a risk index. A lower score means a higher risk.
    return 10 / score

# --- Data Processing and Analysis ---
# Apply the function to each row of the reviews DataFrame to calculate the 'Risk_Index'.
# The lambda function passes the 'Score' and 'Projects' of each row to our decorated function.
df_reviews['Risk_Index'] = df_reviews.apply(lambda row: get_performance_status(score=row['Score'], projects=row['Projects']), axis=1)

# Merge the employee and review DataFrames using a 'left' join.
# This keeps all employees from df_employees and matches them with their review data.
df_final = pd.merge(df_employees, df_reviews, on='EmpID', how='left')

# Fill missing 'Projects' values with 0, assuming no review data means no projects.
df_final['Projects'] = df_final['Projects'].fillna(0)

# --- Filtering and Reporting ---
# Use a list comprehension to find the names of employees who have a low risk index and a high salary.
filtered_employees =  [name for name in df_final[(df_final['Risk_Index'] < 10) & (df_final['Salary'] > 70000)]['Name']]

print("Employees with low risk and high salary:")
print(filtered_employees)

# Group the final DataFrame by 'DeptID' and calculate the average salary for each department.
print("\nAverage Salary by Department:")
avg_salary_by_dept = df_final.groupby('DeptID')['Salary'].mean()
print(avg_salary_by_dept)


