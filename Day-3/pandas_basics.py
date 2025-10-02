# PANDAS BASICS - YOUR TOOL FOR DATA MANIPULATION AND ANALYSIS
# =================================================================
# Pandas is a fast, powerful, and easy-to-use open-source library built on top of NumPy.
# It is the single most important tool for practical, real-world data analysis in Python.
# It introduces two primary data structures that are essential for data science:
#
# 1. `Series`: A one-dimensional labeled array, like a single column in a spreadsheet.
# 2. `DataFrame`: A two-dimensional labeled data structure with columns of potentially different types,
#    much like a spreadsheet, a SQL table, or a dictionary of Series objects.
#
# --- WHY IS PANDAS THE GO-TO LIBRARY FOR DATA ANALYSIS? ---
# • DataFrame Object: Provides a flexible and intuitive way to store and manipulate tabular data.
# • Data I/O: Effortlessly reads and writes data from a wide variety of formats like CSV, Excel, SQL databases, and more.
# • Data Cleaning & Preparation: Offers powerful tools for handling missing data, filtering, sorting, and reshaping data.
# • Powerful Operations: Excels at slicing, dicing, indexing, grouping, merging, and pivoting datasets.
# • Time Series Functionality: Provides robust tools for working with time-series data.
# • Integration: Works seamlessly with other data science libraries like NumPy, Matplotlib, and Scikit-learn.

import pandas as pd  # 'pd' is the standard, community-accepted alias for pandas
import numpy as np   # Import numpy, as it's often used with pandas (e.g., for np.nan)

# ================= CREATING A DATAFRAME =================
print("--- Creating a DataFrame ---")
print("="*60)

# A common way to create a DataFrame is from a Python dictionary where keys become column names
# and lists of values become the data in those columns.
data = {
    'City': ['Istanbul', 'Ankara', 'Izmir', 'Adana'],
    'Population': [15.5, 5.6, 4.3, 2.2],  # in millions
    'Has_Metro': [True, True, False, True]
}

# The `pd.DataFrame()` constructor builds the DataFrame.
df = pd.DataFrame(data)

# The `.head()` method is used to display the first few rows of the DataFrame (default is 5).
# It's a great way to get a quick snapshot of your data.
print("--- Structure Of DataFrame (first 5 rows) ---")
print(df.head())
print("="*60)

# ================= ACCESSING AND INSPECTING DATA =================
print("--- Accessing and Inspecting Data ---")
print("="*60)

# Accessing a single column by its name returns a Pandas `Series`.
print("--- Accessing a single column ('Population') ---")
populations = df['Population']
print(populations)
print(f"Type of a single column: {type(populations)}")

# The `.info()` method provides a concise summary of the DataFrame, including the index dtype,
# column dtypes, non-null values, and memory usage. It's excellent for a quick health check.
print("\n--- DataFrame Info (a quick summary) ---")
df.info()

# The `.describe()` method generates descriptive statistics for the numerical columns.
# This includes count, mean, standard deviation, min, max, and quartiles.
print("\n--- Descriptive Statistics (for numerical columns) ---")
print(df.describe())
print("="*60)


# ================= MODIFYING AND FILTERING DATA =================
print("--- Modifying and Filtering Data ---")
print("="*60)

# --- Adding a New Column ---
# You can easily add a new column. If you assign a single value, it will be "broadcast" to all rows.
df['Continent'] = 'Europe/Asia'
print("--- DataFrame after adding a 'Continent' column ---")
print(df)

# --- Filtering with a Boolean Mask ---
# This is one of the most powerful features of Pandas.
print("\n--- Filtering for cities with population > 5.0 million ---")

# Step 1: Create a boolean mask. This is a Series of True/False values based on a condition.
boolean_mask = df['Population'] > 5.0
print(f"\nGenerated Boolean Mask (condition: Population > 5.0):\n{boolean_mask}")

# Step 2: Use the mask to filter the DataFrame.
# Pandas returns only the rows where the mask's value is `True`.
big_cities_df = df[boolean_mask]
print("\nFiltered DataFrame (only big cities):")
print(big_cities_df)
print("="*60)

# ================= ADVANCED SELECTION WITH .loc and .iloc =================
print("--- Advanced Selection with .loc and .iloc ---")
print("="*60)

# Pandas provides two main methods for precise data selection:
# .loc: Selects data by LABEL (index names, column names). It is inclusive of the end label.
# .iloc: Selects data by INTEGER POSITION (like Python list indexing). It is exclusive of the end position.

print("--- Using .loc (Label-based selection) ---")
# Select the row with the index label `0`.
print(f"Row with index label 0:\n{df.loc[0]}\n")
# Select rows with index labels `0` and `2`, and only the 'City' and 'Population' columns.
print(f"Rows 0 & 2, specific columns 'City' and 'Population':\n{df.loc[[0, 2], ['City', 'Population']]}")

print("\n--- Using .iloc (Integer-position-based selection) ---")
# Select the first row (at integer position 0).
print(f"Row at integer position 0:\n{df.iloc[0]}\n")
# Select the first two rows (positions 0, 1) and the first two columns (positions 0, 1).
print(f"First 2 rows, first 2 columns:\n{df.iloc[0:2, 0:2]}")
print("="*60)

# ================= HANDLING MISSING DATA =================
print("--- Handling Missing Data ---")
print("="*60)

# Real-world data is often messy and contains missing values, represented in Pandas as `np.nan` (Not a Number).
data_with_nan = {
    'A': [1, 2, np.nan, 4],
    'B': [5, np.nan, np.nan, 8],
    'C': [9, 10, 11, 12]
}
df_nan = pd.DataFrame(data_with_nan)
print("--- DataFrame with missing values (NaN) ---")
print(df_nan)

# The `.dropna()` method removes rows (or columns) with any missing values.
print("\n--- Dropping rows with any NaN values ---")
print(df_nan.dropna())

# The `.fillna()` method fills missing values with a specified value.
# A common strategy is to fill with the mean or median of the column.
print("\n--- Filling NaN values with the mean of each respective column ---")
print(df_nan.fillna(df_nan.mean()))
print("="*60)

# ================= SUMMARY OF CONCEPTS =================
print("🎯 CONCEPTS LEARNED:")
print("✓ Creating a `DataFrame` from a dictionary.")
print("✓ Inspecting DataFrames with `.head()`, `.info()`, and `.describe()`.")
print("✓ Accessing columns and understanding that a column is a `Series`.")
print("✓ Adding new columns to a DataFrame.")
print("✓ Filtering data using powerful boolean masks.")
print("✓ Differentiating between `.loc` (label-based) and `.iloc` (integer-based) for precise selection.")
print("✓ Basic strategies for handling missing data with `.dropna()` and `.fillna()`.")
print("="*60)
