# --- Part 1: File I/O with Exception Handling ---
import pandas as pd

# Create a simple DataFrame to be saved as a CSV file.
data_for_csv = pd.DataFrame({'Col1': [1, 2], 'Col2': ['A', 'B']})
# Save the DataFrame to a CSV file named 'sample.csv'.
# 'index=False' prevents pandas from writing row indices into the CSV.
data_for_csv.to_csv('sample.csv', index=False)

# Use a try-except block to safely read the CSV file.
# This allows the program to handle errors gracefully without crashing.
try:
    # Attempt to read the data from 'sample.csv' into a DataFrame.
    df = pd.read_csv('sample.csv')
    print("CSV file read successfully:")
    print(df)
# If the file does not exist, a FileNotFoundError is raised.
except FileNotFoundError:
    print("Error: The file was not found.")
# If the file exists but is empty, pandas raises an EmptyDataError.
except pd.errors.EmptyDataError:
    print("Error: The file is empty.")
# A general 'except' block to catch any other unexpected errors during file processing.
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    
    
# --- Part 2: Exception Handling in Functions ---
print("\nPart 2: Exception Handling in Functions")

# Define a function that performs division but handles potential errors.
def safe_divide(a, b):
    try:
        # Attempt to perform the division.
        return a / b
    # Catch the specific error that occurs when dividing by zero.
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    # Catch the error that occurs if the inputs are of incompatible types (e.g., number and string).
    except TypeError:
        return "Error: Invalid input type. Please provide numbers."

print("\nTesting safe_divide function:")
print(safe_divide(10, 2))      # Expected output: 5.0
print(safe_divide(10, 0))      # Expected output: Error message for division by zero.
print(safe_divide(10, 'a'))    # Expected output: Error message for invalid type.


# --- Practice: Combining File I/O and Exception Handling ---
print("\nPractice: File Processing with Exception Handling")

# Define a function that reads and processes a file, including error handling.
def process_file(file_path: str):
    try:
        # Attempt to read the CSV file at the given path.
        read_pd = pd.read_csv(file_path)
        print(f"File '{file_path}' processed successfully.")
        # Display the first few rows of the DataFrame.
        print(read_pd.head())
    # Handle the case where the file is not found.
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    # Catch any other exceptions that might occur.
    except Exception as e:
        print(f"An unexpected error occurred while processing '{file_path}': {e}")

# Test the function with a file that exists.
process_file('sample.csv')
print("-----------------")
# Test the function with a file that does not exist to see error handling in action.
process_file('non_existent_file.csv')


