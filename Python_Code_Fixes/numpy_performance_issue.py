"""
PROBLEM: NumPy Performance Issue - Using Loops Instead of Vectorization
========================================================================
NumPy is designed for vectorized operations that work on entire arrays at once.
Using Python for-loops to iterate through NumPy arrays defeats this purpose and
results in dramatically slower performance (often 10-100x slower).

ISSUE DEMONSTRATION (Commented Code Below):
- Creating 1,000,000 element arrays
- Using a for-loop to multiply corresponding elements
- This approach is slow because it uses Python-level iteration
- Each iteration involves Python overhead (type checking, function calls, etc.)

# numpy_performance_issue.py
import numpy as np
import time

# 1,000,000 rows of random data
data_size = 1000000 
column_a = np.random.rand(data_size)
column_b = np.random.rand(data_size)

# Error/Inefficiency: Using for-loops with NumPy arrays is extremely slow
def calculate_product_slow(a, b):
    result = []
    # ❌ Anti-Pattern: Not leveraging NumPy's vectorization power
    # This loop processes one element at a time at Python level
    for i in range(len(a)):
        result.append(a[i] * b[i])
    return np.array(result)

start_time = time.time()
product_result = calculate_product_slow(column_a, column_b)
end_time = time.time()

print(f"Computation Time: {end_time - start_time:.4f} seconds")  # Very slow!
print(f"Result Shape: {product_result.shape}")

"""

# SOLUTION: Using NumPy Vectorization
# ====================================
# NumPy's vectorized operations are implemented in optimized C code
# They process entire arrays in a single operation, which is much faster
# This approach can be 10-100x faster than using Python loops

import numpy as np
import time

# Generate 1,000,000 rows of random data
data_size = 1000000 
column_a = np.random.rand(data_size)
column_b = np.random.rand(data_size)

# Fix: Use NumPy's vectorized multiplication
def calculate_product_fast(a, b):
    """
    Multiplies two NumPy arrays element-wise using vectorization.
    
    Args:
        a: First NumPy array
        b: Second NumPy array
        
    Returns:
        NumPy array containing element-wise product
    """
    # Vectorized operation: multiplies all elements at once
    # No explicit loop needed - NumPy handles this efficiently in C
    result = np.array(a * b)
    return result

start_time = time.time()
product_result = calculate_product_fast(column_a, column_b)
end_time = time.time()

print(f"Computation Time: {end_time - start_time:.4f} seconds")  # Much faster!
print(f"Result Shape: {product_result.shape}")