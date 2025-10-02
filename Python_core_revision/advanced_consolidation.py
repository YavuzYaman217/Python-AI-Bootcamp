# This script demonstrates advanced data manipulation techniques using pandas and Python's built-in features.
# It covers creating a DataFrame, applying vectorized functions, flattening lists with list comprehensions,
# aggregating data, and conditional filtering.

import pandas as pd
import numpy as np # Import NumPy for potential future use/habit

# 1. Data Setup (Veri Seti Kurulumu)
# A raw dataset is created as a Python dictionary.
# This dictionary is then used to initialize a pandas DataFrame, which is a 2D labeled data structure.
data = {
    'CustomerID': [101, 102, 103, 104, 105, 106, 107],
    'Item_List': ['Apple,Banana,Milk', 'Book,Pen', 'Milk,Bread,Cheese,Milk', 'Water', 'Banana,Apple', '', 'Pen,Book,Pen'],
    'Discount_Code': ['WELCOME20', 'NONE', 'SEPTSALE', 'NULL', 'WELCOME20', 'NONE', 'SEPTSALE'],
    'Total_Price': [55.50, 120.00, 32.80, 5.00, 45.00, 0.00, 115.00]
}
df_raw = pd.DataFrame(data)

# --- 2. NumPy/Pandas Vektorizasyon ve Fonksiyon ---
# Vectorization allows applying an operation to an entire array (or pandas Series) at once,
# which is significantly faster than iterating through each element.

def calculate_tax(price: float, tax_rate: float = 0.18) -> float:
    """Calculates the total price including VAT (18% by default)."""
    # This function takes a price and a tax rate, returning the price with tax included.
    return price * (1 + tax_rate)

# Applying the function directly to the 'Total_Price' Series.
# Pandas automatically applies the 'calculate_tax' function to each element in the Series.
# A new column 'Final_Price_Tax' is created to store the results.
df_raw['Final_Price_Tax'] = calculate_tax(df_raw['Total_Price'])

print("--- DataFrame after Tax Calculation ---")
print(df_raw)
print("-" * 60)

# --- 3. List Comprehension for Flattening (Liste Kapsaması ile Düzleştirme) ---
# List comprehensions provide a concise way to create lists.
# Here, it's used to 'flatten' a list of lists into a single list.

# The 'Item_List' column contains comma-separated strings.
# This list comprehension iterates through each string in 'Item_List'.
# It splits the string into individual items and strips any whitespace.
# The result is a single flat list containing all items from all customers.
all_items_list = [
    item.strip() # Strip whitespace from each item.
    for item_str in df_raw['Item_List'] 
    if item_str # Process only non-empty strings.
    for item in item_str.split(',') # Split the string by comma and iterate through the items.
]

print("--- All Items in a Single Python List (Flattened) ---")
print(all_items_list)
print("-" * 60)

# --- 4. Dict Comprehension and Aggregation (Sözlük Kapsaması ve Agregasyon) ---
# Dictionary comprehensions are a concise way to create dictionaries.
# Here, we first aggregate data and then convert it into a dictionary.

# Filter the DataFrame to exclude rows where 'Discount_Code' is 'NONE' or 'NULL'.
# The '~' operator negates the boolean Series returned by isin().
valid_codes_df = df_raw[~df_raw['Discount_Code'].isin(['NONE', 'NULL'])]

# 'value_counts()' is used to count the occurrences of each unique 'Discount_Code'.
code_counts = valid_codes_df['Discount_Code'].value_counts()

# A dictionary comprehension is used to convert the resulting pandas Series into a Python dictionary.
# It iterates through the items (code, count) of the 'code_counts' Series.
discount_counts_dict = {
    code: count 
    for code, count in code_counts.items()
}

print("--- Discount Codes Usage Count (Dict Comprehension) ---")
print(discount_counts_dict)
print("-" * 60)

# --- 5. Conditional DataFrame Filtering ---
# Filtering a DataFrame based on one or more conditions is a common operation.

# A boolean mask is created. This is a pandas Series of True/False values.
# The '&' operator performs an element-wise 'AND' operation.
# The mask will be 'True' for rows where 'Total_Price' is greater than 50 AND 'Discount_Code' is 'WELCOME20'.
boolean_mask = (df_raw['Total_Price'] > 50.00) & (df_raw['Discount_Code'] == 'WELCOME20')

# The boolean mask is used to select rows from the DataFrame.
# Only rows where the mask is 'True' will be included in the new 'filtered_df'.
filtered_df = df_raw[boolean_mask]

print("--- Filtered DataFrame (Price > 50 AND Code = 'WELCOME20') ---")
print(filtered_df)
print("-" * 60)