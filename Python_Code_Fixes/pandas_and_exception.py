"""
PROBLEM: Inefficient Exception Handling and Non-Vectorized Operations in Pandas
================================================================================
When working with Pandas DataFrames, using row-by-row operations (like apply with lambda)
is significantly slower than vectorized operations. Additionally, handling edge cases
(like division by zero) with if-statements inside apply is inefficient.

ISSUE DEMONSTRATION (Commented Code Below):
1. Using apply() with lambda for row-wise operations - slow for large datasets
2. Using if-statement for zero-checking instead of exception handling
3. Not leveraging NumPy's vectorized operations for conditional logic

# pandas_and_exception.py
import pandas as pd

data = {'SaleID': [1, 2, 3, 4],
        'Sales': [100.0, 50.0, 0.0, 200.0],  # Potential error: SaleID 3 has zero sales!
        'Discount': [10.0, 5.0, 2.0, 20.0]}
df = pd.DataFrame(data)

def calculate_discount_rate(sale_amount, discount_amount):
    # Error 1: This method is not Pythonic and slow
    # Using if-statement for validation is slower than exception handling
    if sale_amount == 0:
        return 0.0
    return discount_amount / sale_amount

# Error 2: Using apply() for row-wise operations - very slow!
# apply() with lambda processes each row individually at Python level
df['Rate'] = df.apply(lambda row: calculate_discount_rate(row['Sales'], row['Discount']), axis=1)

print(df)
# Expected Output (with error handling for SaleID 3): 0.10, 0.10, 0.00, 0.10

"""

# SOLUTION: Using Vectorized Operations with NumPy
# =================================================
# NumPy's np.where() and vectorized division are much faster than apply()
# This approach handles the entire column at once, avoiding Python-level iteration

import pandas as pd
import numpy as np
import time as time

# Sample sales data with a potential division-by-zero case
data = {'SaleID': [1, 2, 3, 4],
        'Sales': [100.0, 50.0, 0.0, 200.0],  # SaleID 3 has zero sales
        'Discount': [10.0, 5.0, 2.0, 20.0]}
df = pd.DataFrame(data)

def calculate_discount_rate(sale_amount, discount_amount):
    """
    Calculates discount rate with proper exception handling.
    
    Args:
        sale_amount: Sales amount
        discount_amount: Discount amount
        
    Returns:
        Discount rate or 0.0 if division by zero occurs
    """
    # Using try-except is more Pythonic and handles edge cases gracefully
    try:
        return discount_amount / sale_amount
    except ZeroDivisionError:
        return 0.

# Measure performance of vectorized approach
start_time = time.time()

# Fix: Use NumPy's np.where() for conditional vectorized operations
# This is much faster than apply() as it operates on entire columns at once
# Syntax: np.where(condition, value_if_true, value_if_false)
df['Rate'] = np.where(df['Sales'] == 0, 0.0, df['Discount'] / df['Sales'])

# Alternative (commented): Using np.vectorize() - slightly slower but still better than apply()
# df['Rate'] = np.vectorize(calculate_discount_rate)(df['Sales'], df['Discount']) 

end_time = time.time()

print("Vectorized approach time:", end_time - start_time)
print(df)
