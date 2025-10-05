"""
PROBLEM: Decorator Scope Error - Function Metadata Loss
========================================================
When creating decorators in Python, a common mistake is not preserving the original
function's metadata (name, docstring, module, etc.). Without using @wraps from functools,
the decorator's wrapper function replaces the original function's identity.

ISSUE DEMONSTRATION (Commented Code Below):
- A timer decorator is created to measure function execution time
- The wrapper function inside the decorator doesn't preserve metadata
- When you check analyze_data.__name__, it returns 'wrapper' instead of 'analyze_data'
- The original docstring is also lost

# decorator_scope_error.py
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time:.4f} seconds")
        return result
    # Error: Wrapper hides the wrapped function's name and documentation
    return wrapper

@timer
def analyze_data(n):
    Analyzes large dataset and returns the result.
    # Simple simulation
    return sum(x * 2 for x in range(n))

# Check the function's name and documentation:
print(f"Function Name: {analyze_data.__name__}")  # Would print 'wrapper' (WRONG!)
print(f"Function Documentation: {analyze_data.__doc__}")  # Would print None (WRONG!)

# Expected Output:
# Function Name: analyze_data
# Function Documentation: Analyzes large dataset and returns the result.
"""

# SOLUTION: Using @wraps decorator from functools
# ================================================
# The @wraps decorator copies metadata from the original function to the wrapper function
# This preserves __name__, __doc__, __module__, __annotations__, and other attributes

import time
from functools import wraps  # Import wraps to preserve function metadata

def timer(func):
    """
    Decorator that measures and prints the execution time of a function.
    Uses @wraps to preserve the original function's metadata.
    """
    @wraps(func)  # This decorator preserves func's metadata on the wrapper
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@timer
def analyze_data(n):
    """Analyzes large dataset and returns the result."""
    return sum(x * 2 for x in range(n))

# Now the function's metadata is correctly preserved
print(f"Function Name: {analyze_data.__name__}")  # Prints: analyze_data (CORRECT!)
print(f"Function Documentation: {analyze_data.__doc__}")  # Prints the docstring (CORRECT!)
