"""
PROBLEM: Pandas Iteration Error - Using iterrows() for Row-by-Row Operations
=============================================================================
One of the most common performance mistakes in Pandas is using iterrows() to iterate
through DataFrame rows. This method is extremely slow because it:
1. Converts each row to a Series object (overhead)
2. Processes data at Python level (not optimized C code)
3. Loses the benefit of vectorized operations

For operations on 10,000 rows, iterrows() can be 100-1000x slower than vectorized operations!

ISSUE DEMONSTRATION (Commented Code Below):
- Creating a DataFrame with 10,000 rows
- Using iterrows() to calculate Total = Price * Quantity for each row
- This approach is very slow and not recommended

# pandas_iteration_error.py
import pandas as pd
import numpy as np
import time

data = {'Price': np.random.randint(10, 100, 10000),
        'Quantity': np.random.randint(1, 10, 10000)}
df = pd.DataFrame(data)

# Error: Using row-by-row iteration in Pandas is extremely slow
def calculate_total_slow(df):
    total_list = []
    # ❌ Anti-Pattern: iterrows() is one of the slowest methods in Pandas
    # Each iteration creates a Series object and processes data at Python level
    for index, row in df.iterrows(): 
        total_list.append(row['Price'] * row['Quantity'])
    df['Total'] = total_list
    return df

start_time = time.time()
df_slow = calculate_total_slow(df.copy())  # copy() preserves data integrity
end_time = time.time()

print(f"Slow Computation Time (iterrows): {end_time - start_time:.4f} seconds")
print(df_slow.head())
"""

# SOLUTION: Using Vectorized Operations
# ======================================
# Pandas is built on top of NumPy and supports vectorized operations
# These operations work on entire columns at once and are implemented in C
# Result: 100-1000x faster than iterrows()!

import pandas as pd
import numpy as np
import time

# Create sample data with 10,000 rows
data = {'Price': np.random.randint(10, 100, 10000),
        'Quantity': np.random.randint(1, 10, 10000)}
df = pd.DataFrame(data)

# Slow approach (for comparison): Using iterrows()
def calculate_total_slow(df):
    """
    Calculates total using iterrows() - NOT RECOMMENDED!
    
    This is kept for performance comparison purposes.
    """
    total_list = []
    # ❌ Anti-Pattern: iterrows() is extremely slow
    for index, row in df.iterrows(): 
        total_list.append(row['Price'] * row['Quantity'])
    df['Total'] = total_list
    return df

# Fix: Fast approach using vectorized operations
def calculate_total_fast(df):
    """
    Calculates total using vectorized operations - RECOMMENDED!
    
    This approach multiplies entire columns at once, which is much faster.
    Args:
        df: DataFrame with Price and Quantity columns
        
    Returns:
        DataFrame with added Total column
    """
    # Vectorized operation: multiplies entire columns in one operation
    # This uses optimized C code under the hood
    df['Total'] = df['Price'] * df['Quantity']
    return df

# Performance comparison
start_time = time.time()
df_slow = calculate_total_slow(df.copy())  # copy() preserves original data
end_time = time.time()
print(f"Slow Computation Time (iterrows): {end_time - start_time:.4f} seconds")
print(df_slow.head())

start_time = time.time()
df_fast = calculate_total_fast(df.copy())
end_time = time.time()
print(f"Fast Computation Time: {end_time - start_time:.4f} seconds")
print(df_fast.head())

# The vectorized approach is typically 100-1000x faster!
