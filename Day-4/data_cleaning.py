# Import necessary libraries: pandas for data manipulation and numpy for numerical operations.
import pandas as pd
import numpy as np

# --- Handling Missing Data ---

# Create a sample DataFrame 'df1' with some missing data (np.nan).
df1 = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'Name': ['Ali', 'Buse', 'Can', 'Deniz'],
    'Score': [85, 92, np.nan, 78]  # 'Can' has a missing score.
})

# Check for missing values in the DataFrame.
# .isnull() returns a boolean DataFrame of the same size, indicating where values are missing.
# .sum() then counts the number of True values (missing values) for each column.
print(f"Missing values in df1:\n{df1.isnull().sum()}\n")

# Impute missing values. A common strategy is to fill them with the mean of the column.
# Calculate the average of the 'Score' column, ignoring the NaN value.
avg_score = df1['Score'].mean()
# Use .fillna() to replace all NaN values in the 'Score' column with the calculated average.
df1['Score'] = df1['Score'].fillna(avg_score)
print(f"DataFrame after filling missing values:\n{df1}\n")



#-------Merging and Cleaning Example--------

# Create a DataFrame with student information.
df_students = pd.DataFrame({'StudentID': [101, 102, 103, 104],
                            'Name': ['Ece', 'Fikret', 'Gizem', 'Hakan']})

# Create another DataFrame with student scores, including missing values.
df_scores = pd.DataFrame({'StudentID': [101, 102, 103, 104],
                          'MathScore' : [90, 85, 88, 92],
                          'SciScore': [np.nan, 80, np.nan, 90]}) # Two students have missing science scores.

# Fill missing science scores with 0. This might be appropriate if a missing score means the test wasn't taken.
df_scores['SciScore'] = df_scores['SciScore'].fillna(0)

# Merge (join) the two DataFrames based on the common 'StudentID' column.
# This combines the student names and their scores into a single DataFrame.
df_merged = pd.merge(df_students, df_scores, on='StudentID')
print(f"Merged DataFrame:\n{df_merged}\n")