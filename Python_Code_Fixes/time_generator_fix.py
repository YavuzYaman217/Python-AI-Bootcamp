"""
PROBLEM 1: Memory-Inefficient List Creation
============================================
Creating large lists in memory can consume significant RAM and cause performance issues.
For example, a list of 5,000,000 integers can use hundreds of megabytes of memory.
When you only need to iterate through values once, using a generator is much more efficient.

PROBLEM 2: Incorrect Time Series Resampling Method
===================================================
When working with time series data in Pandas, using groupby() with pd.Grouper() for
resampling is unnecessarily complex. The resample() method is specifically designed
for time series operations and is more intuitive and efficient.

ISSUE DEMONSTRATION (Commented Code Below):

# time_generator_fix.py
import pandas as pd
import numpy as np

# Error 1: List comprehension loads all 5 million items into memory at once
def massive_data_processor():
    # This creates a list with 5,000,000 elements - uses ~200MB+ of memory!
    return [i * 10 for i in range(5000000)] 

# Error 2: Using groupby instead of resample for time series
dates = pd.date_range('2024-01-01', periods=90, freq='D')
temps = np.random.randint(5, 30, 90)
df_weather = pd.DataFrame({'Date': dates, 'Temp': temps}).set_index('Date')

# This works but is unnecessarily complex for time series resampling
monthly_avg_temp = df_weather.groupby(pd.Grouper(freq='ME'))['Temp'].mean()

# print(monthly_avg_temp)
"""

# SOLUTIONS: Using Generator Expression and Proper Time Series Methods
# =====================================================================

# SOLUTION 1: Generator Expression for Memory Efficiency
# -------------------------------------------------------
# Generators produce values on-the-fly, one at a time, instead of storing all in memory
# Memory usage: constant (a few bytes) regardless of how many values are generated

import pandas as pd
import numpy as np

def massive_data_processor():
    """
    Returns a generator that produces 5,000,000 values on-demand.
    
    Generator benefits:
    - Memory efficient: only stores one value at a time
    - Lazy evaluation: values computed only when requested
    - Perfect for one-time iteration (e.g., in for-loops)
    
    Returns:
        Generator object that yields values
    """
    # Generator Expression: uses parentheses () instead of brackets []
    # This creates a generator object, not a list
    # Memory usage: ~100 bytes vs ~200MB for list!
    return (i * 10 for i in range(5000000))  # Generator Expression

# SOLUTION 2: Using resample() for Time Series Operations
# --------------------------------------------------------
# The resample() method is specifically designed for time series resampling
# It's more intuitive, cleaner, and explicitly shows temporal aggregation intent

# Generate 90 days of temperature data (January-March 2024)
dates = pd.date_range('2024-01-01', periods=90, freq='D')
temps = np.random.randint(5, 30, 90)

# Create DataFrame with Date as index (required for resample)
df_weather = pd.DataFrame({'Date': dates, 'Temp': temps}).set_index('Date')

# Fix: Use resample() method for time series aggregation
# 'ME' = Month End frequency (replaces deprecated 'M')
# This groups data by month and calculates mean temperature for each month
monthly_avg_temp = df_weather.resample('ME').mean()

print(monthly_avg_temp)

# Note: resample() is specifically designed for time series and offers:
# - Cleaner syntax than groupby
# - Built-in time-aware aggregation
# - Better performance for temporal operations