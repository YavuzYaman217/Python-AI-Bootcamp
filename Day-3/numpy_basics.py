# NUMPY BASICS - THE FOUNDATION OF SCIENTIFIC COMPUTING IN PYTHON
# =================================================================
# NumPy (Numerical Python) is the most important foundational library for numerical and scientific computing in Python.
# It introduces the powerful N-dimensional array object (`ndarray`), which provides fast and memory-efficient
# storage for large datasets, along with a vast collection of mathematical functions to operate on these arrays.
#
# --- WHY IS NUMPY ESSENTIAL FOR DATA SCIENCE? ---
# • Performance: NumPy arrays are implemented in C and are significantly faster for mathematical operations
#   than standard Python lists. They also consume less memory.
# • Vectorization: NumPy allows you to perform operations on entire arrays at once without writing explicit
#   loops in Python. This "vectorized" code is more concise, more readable, and much faster.
# • Mathematical Functions: It offers a comprehensive library of functions for linear algebra, statistics,
#   Fourier transforms, random number generation, and more.
# • Ecosystem Foundation: NumPy is the bedrock upon which most of the Python data science ecosystem is built.
#   Libraries like Pandas, SciPy, Matplotlib, and Scikit-learn all rely on NumPy arrays.

import numpy as np  # 'np' is the universally accepted alias for numpy

# ================= PYTHON LISTS vs. NUMPY ARRAYS =================
print("--- Python List vs. NumPy Array Operations ---")
print("="*60)

# --- Standard Python List Behavior ---
# When you "multiply" a Python list, it duplicates its elements, which is often not the desired mathematical outcome.
my_list = [1, 2, 3, 4, 5]
print(f"A standard Python list: {my_list}")
print(f"Python list * 2 (duplicates elements): {my_list * 2}")

# --- NumPy Array Behavior (Vectorization) ---
# A NumPy array enables true mathematical operations on its elements.
py_list = [1, 2, 3, 4, 5]
my_array = np.array(py_list)  # Create a NumPy array from a Python list

print(f"\nA NumPy array: {my_array}")
print(f"Data type of array elements: {my_array.dtype}")  # e.g., int32, float64
print(f"Shape of the array (rows, columns): {my_array.shape}")  # (5,) means a 1D array with 5 elements

# --- VECTORIZED OPERATION IN ACTION ---
# The multiplication operation is applied element-wise to the entire array without a Python loop.
# This is the core concept of vectorization.
new_array = my_array * 2
print(f"NumPy array * 2 (mathematical operation): {new_array}")
print("="*60)

# ================= MULTI-DIMENSIONAL ARRAYS (MATRICES) =================
print("--- Multi-Dimensional Arrays (Matrices) ---")
print("="*60)

# Creating a 2D array (often called a matrix) from a list of lists.
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(f"A 2D Matrix (2 rows, 3 columns):\n{matrix}")
print(f"Shape of the matrix: {matrix.shape}")  # Returns a tuple (rows, columns)

# Applying a "universal function" (ufunc) like `np.sqrt` to the entire matrix.
# Ufuncs are functions that operate on ndarrays in an element-by-element fashion.
print(f"\nSquare root of every element in the matrix:\n{np.sqrt(matrix)}")
print("="*60)

# ================= ARRAY CREATION AND RESHAPING =================
print("--- Array Creation and Reshaping ---")
print("="*60)

# `np.arange()` is NumPy's version of Python's `range()`, but it returns a NumPy array.
my_matrix = np.arange(12)  # Creates a 1D array with integers from 0 to 11.
print(f"1D array created with np.arange(12): {my_matrix}")

# The `.reshape()` method changes the shape of an array without changing its data.
# The new shape must be compatible with the original size (e.g., 3 * 4 = 12).
my_matrix = my_matrix.reshape(3, 4)  # Reshape into a 3x4 matrix.
print(f"\nReshaped into a 3x4 matrix:\n{my_matrix}")

# Another example of a vectorized operation: adding 5 to every element.
print(f"\nMatrix + 5 (adds 5 to each element):\n{my_matrix + 5}")
print("="*60)

# ================= OTHER USEFUL NUMPY CREATION FUNCTIONS =================
print("--- Other Useful NumPy Creation Functions ---")
print("="*60)

# Create an array of all zeros with a given shape.
zeros = np.zeros((2, 3))  # Shape is a tuple: (2 rows, 3 columns)
print(f"An array of zeros (2x3):\n{zeros}")

# Create an array of all ones.
ones = np.ones((3, 2))  # Shape is (3 rows, 2 columns)
print(f"\nAn array of ones (3x2):\n{ones}")

# `np.linspace()` creates an array with a specified number of points, evenly spaced between two values.
linspace_arr = np.linspace(0, 10, 5)  # Start, Stop, Number of points
print(f"\nAn array with 5 evenly spaced points from 0 to 10: {linspace_arr}")

# `np.eye()` creates an identity matrix (a square matrix with ones on the diagonal and zeros elsewhere).
identity_matrix = np.eye(3)  # Creates a 3x3 identity matrix.
print(f"\nA 3x3 Identity Matrix:\n{identity_matrix}")

# Create an array with random values from a uniform distribution over [0, 1).
random_arr = np.random.rand(2, 3)  # Creates a 2x3 array.
print(f"\nA 2x3 array of random values between 0 and 1:\n{random_arr}")
print("="*60)

# ================= ARRAY INDEXING AND SLICING =================
print("--- Array Indexing and Slicing ---")
print("="*60)

arr = np.arange(10)
print(f"Original 1D array: {arr}")

# Basic indexing and slicing work just like Python lists.
print(f"Element at index 3: {arr[3]}")
print(f"Elements from index 2 up to (but not including) 5: {arr[2:5]}")

# Broadcasting: efficiently setting multiple elements to the same value.
arr[0:5] = 100
print(f"Array after broadcasting 100 to the first 5 elements: {arr}")

# --- Indexing in 2D Arrays ---
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"\nOriginal 2D Matrix:\n{matrix}")
# Use `[row, column]` to access individual elements.
print(f"Element at row 1, column 2: {matrix[1, 2]}")  # Gets the value 6
# Get an entire row or column.
print(f"The first row: {matrix[0]}")
print(f"The first column: {matrix[:, 0]}")  # The ':' means "all rows".

# --- Conditional Selection (Boolean Indexing) ---
# This is a very powerful feature for filtering data.
# Create a boolean array based on a condition.
bool_arr = matrix > 5
print(f"\nBoolean mask where elements > 5:\n{bool_arr}")
# Use this boolean array to select only the elements from the original matrix that are `True`.
print(f"Values from the matrix where the condition is True: {matrix[bool_arr]}")
print("="*60)

# ================= BASIC MATH AND STATISTICAL OPERATIONS =================
print("--- Basic Math and Statistical Operations ---")
print("="*60)
stats_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(f"Statistical analysis on array: {stats_array}")
print(f"Sum of all elements: {stats_array.sum()} or {np.sum(stats_array)}")
print(f"Mean (average) of all elements: {stats_array.mean()}")
print(f"Standard deviation: {stats_array.std():.2f}")
print(f"Maximum value: {stats_array.max()}")
print(f"Minimum value: {stats_array.min()}")
print("="*60)

# ================= SUMMARY OF CONCEPTS =================
print("🎯 CONCEPTS LEARNED:")
print("✓ Creating NumPy arrays from Python lists and the benefits of doing so.")
print("✓ Vectorized operations (e.g., `array * 2`) for fast, element-wise math.")
print("✓ Multi-dimensional arrays (matrices) and understanding their `.shape`.")
print("✓ Using universal functions (ufuncs) like `np.sqrt`.")
print("✓ Array creation functions: `arange`, `zeros`, `ones`, `linspace`, `eye`, `random`.")
print("✓ Reshaping arrays with `.reshape()`.")
print("✓ Indexing, slicing, and broadcasting for data access and modification.")
print("✓ Powerful conditional selection with boolean arrays.")
print("✓ Basic statistical methods like `.mean()`, `.sum()`, and `.std()`.")
print("="*60)





