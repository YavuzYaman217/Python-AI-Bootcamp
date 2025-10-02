# PYTHON'S FUNCTIONAL TOOLKIT: LAMBDA, MAP, AND FILTER
# ==============================================================
# This file explores some of Python's functional programming tools. Functional programming is a
# programming paradigm that treats computation as the evaluation of mathematical functions and
# avoids changing-state and mutable data.
#
# - `lambda`: Creates small, anonymous (unnamed) functions for simple, one-line operations.
# - `map()`: Applies a given function to every item in an iterable (like a list) and returns a map object (which can be converted to a list).
# - `filter()`: Constructs an iterator from elements of an iterable for which a function returns true.
#
# These tools are powerful for concise and efficient data processing, often used together.

# --- LAMBDA FUNCTIONS: QUICK, ANONYMOUS FUNCTIONS ---
# SYNTAX: lambda arguments: expression
#
# Key Characteristics:
# • Anonymous: No function name is defined with `def`.
# • Single Expression: Can only contain one expression, which is automatically returned.
# • Inline: Often defined right where they are needed, improving local readability.
# • Use Case: Ideal for short, simple functions that are used only once, especially as arguments to other functions like map() and filter().
#=================EXAMPLE 1: BASIC LAMBDA FUNCTIONS=================
print("--- Example 1: Basic Lambda Functions ---")
print("="*60)

# A lambda function can be assigned to a variable, but this is often just for demonstration.
# Its main power comes from being used directly without assignment.
add_ten = lambda x: x + 10
print(f"Calling a lambda via a variable: add_ten(5) = {add_ten(5)}")

# --- COMPARISON: Lambda vs. Regular Function ---
# Lambda version (concise, one-line):
multiply = lambda x, y: x * y

# Equivalent regular function (more verbose, but needed for complex logic):
def multiply_regular(x, y):
    """This is a standard function that multiplies two numbers."""
    return x * y

print(f"Lambda result: multiply(3, 4) = {multiply(3, 4)}")
print(f"Regular function result: multiply_regular(3, 4) = {multiply_regular(3, 4)}")

# --- LAMBDA SYNTAX BREAKDOWN ---
# lambda x, y: x * y
# │      │      └─ Expression: The operation to perform. Its result is automatically returned.
# │      └─ Arguments: The input parameters for the function.
# └─ Keyword: Defines an anonymous function.
print("="*60)

#=================EXAMPLE 2: MORE LAMBDA EXAMPLES=================
print("--- Example 2: More Lambda Variations ---")

# Single parameter lambda
square = lambda x: x ** 2
print(f"Square of 5: {square(5)}")

# Multiple parameters
power = lambda base, exp: base ** exp
print(f"2 to the power of 3: {power(2, 3)}")

# Lambda with a conditional expression (ternary operator)
# This is a common pattern for simple if-else logic within a lambda.
absolute_value = lambda x: x if x >= 0 else -x
print(f"Absolute value of -7: {absolute_value(-7)}")
print(f"Absolute value of 7: {absolute_value(7)}")

# Lambda with string operations
full_name = lambda first, last: f"{first} {last}".title()
print(f"Formatted full name: '{full_name('john', 'doe')}'")
print("="*60)

#=================EXAMPLE 3: THE MAP() FUNCTION=================
print("--- Example 3: map() - Applying a Function to All Items ---")

# `map()` takes a function and an iterable, and applies the function to every item.
# It returns a `map` object, which is an iterator. We use `list()` to see the results immediately.
data = [1, 5, 8, 12, 15]

# Using map() with a pre-defined lambda
squared_list = list(map(square, data))
print(f"Original data: {data}")
print(f"Squared with map():  {squared_list}")

# Using map() with an inline lambda (the most common use case)
cubed_list = list(map(lambda x: x**3, data))
print(f"Cubed with map():    {cubed_list}")

# --- MAP() SYNTAX BREAKDOWN ---
# map(function, iterable)
#     │         └─ The data to process (e.g., a list).
#     └─ The function to apply to each item.

# `map()` can also work with multiple iterables.
numbers1 = [1, 2, 3, 4]
numbers2 = [10, 20, 30, 40]
sums = list(map(lambda x, y: x + y, numbers1, numbers2))
print(f"Adding corresponding elements from two lists: {sums}")

# --- MAP vs. LIST COMPREHENSION ---
# List comprehensions are often considered more "Pythonic" and readable for the same task.
print("\n--- Map vs. List Comprehension ---")
map_result = list(map(lambda x: x * 2, data))
comprehension_result = [x * 2 for x in data]
print(f"Map result:           {map_result}")
print(f"Comprehension result: {comprehension_result}")
print(f"Results are identical: {map_result == comprehension_result}")
print("="*60)

#=================EXAMPLE 4: THE FILTER() FUNCTION=================
print("--- Example 4: filter() - Selecting Items That Meet Criteria ---")

# `filter()` creates an iterator from elements of an iterable for which the provided function returns `True`.
data = [1, 5, 8, 12, 15, 20, 7, 4]

# Filter for even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, data))
print(f"Original data:  {data}")
print(f"Even numbers:   {even_numbers}")

# Filter for numbers greater than 10
large_numbers = list(filter(lambda x: x > 10, data))
print(f"Numbers > 10:   {large_numbers}")

# --- FILTER() SYNTAX BREAKDOWN ---
# filter(function, iterable)
#        │         └─ The data to test.
#        └─ A function that returns True (keep) or False (discard).

# Filtering with more complex conditions
words = ["apple", "banana", "cherry", "date", "elderberry"]
long_words = list(filter(lambda word: len(word) > 5, words))
print(f"Words longer than 5 letters: {long_words}")

# --- FILTER vs. LIST COMPREHENSION ---
# Again, list comprehensions are often preferred for readability.
print("\n--- Filter vs. List Comprehension ---")
filter_result = list(filter(lambda x: x > 7, data))
comprehension_result = [x for x in data if x > 7]
print(f"Filter result:        {filter_result}")
print(f"Comprehension result: {comprehension_result}")
print(f"Results are identical: {filter_result == comprehension_result}")
print("="*60)

#=================EXAMPLE 5: COMBINING MAP AND FILTER=================
print("--- Example 5: Combining map() and filter() ---")

numbers = range(1, 11)  # Represents [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# GOAL: Get the squares of all even numbers from 1 to 10.
# Method 1: Chaining map() and filter()
# The output of filter() is fed directly into map().
result = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers)))
print(f"Chained map/filter result: {result}")

# Method 2: Using a list comprehension (often more readable)
comprehension_equivalent = [x**2 for x in numbers if x % 2 == 0]
print(f"List comprehension result: {comprehension_equivalent}")

# Real-world example: Process a list of names
names = ["alice", "bob", "charlie", "diana", "eve"]
# GOAL: Capitalize names that are longer than 3 characters.
processed_names = list(map(lambda name: name.capitalize(), 
                          filter(lambda name: len(name) > 3, names)))
print(f"Long names capitalized: {processed_names}")
print("="*60)

#=================PRACTICAL APPLICATIONS=================
print("--- Real-World Applications ---")

# Data processing pipeline for sales data
sales_data = [120, 85, 200, 45, 160, 90, 180]

# GOAL: Find high-performing sales (>100) and calculate a 10% bonus for them.
high_sales = list(filter(lambda x: x > 100, sales_data))
bonuses = list(map(lambda x: x * 0.1, high_sales))
print(f"Original sales data: {sales_data}")
print(f"High-performing sales (>100): {high_sales}")
print(f"Calculated bonuses (10%): {[f'{b:.2f}' for b in bonuses]}")

# Working with a list of dictionaries
employees = [
    {"name": "Alice", "salary": 50000, "department": "IT"},
    {"name": "Bob", "salary": 60000, "department": "HR"},
    {"name": "Charlie", "salary": 70000, "department": "IT"},
]

# GOAL: Get the names of all employees in the IT department.
it_employees = list(map(lambda emp: emp["name"], 
                       filter(lambda emp: emp["department"] == "IT", employees)))
print(f"Names of IT employees: {it_employees}")
print("="*60)

#=================WHEN TO USE WHAT=================
print("🎯 WHEN TO USE EACH APPROACH:")
print()
print("LAMBDA FUNCTIONS:")
print("  ✅ Use for short, simple, one-line functions.")
print("  ✅ Perfect for use with `map`, `filter`, `sorted`, etc.")
print("  ❌ Avoid for complex logic; use a `def` function instead for readability.")
print()
print("MAP():")
print("  ✅ Use when you need to transform every item in a collection using the same operation.")
print("  ✅ Good when you already have an existing function to apply.")
print("  🤔 Often, a list comprehension is more readable and preferred.")
print()
print("FILTER():")
print("  ✅ Use when you need to select a subset of items based on a condition.")
print("  🤔 A list comprehension with an `if` clause is often clearer.")
print()
print("LIST COMPREHENSIONS:")
print("  ✅ The most 'Pythonic' and readable choice for simple map and filter operations.")
print("  ✅ Excellent for combining both mapping and filtering in one line (e.g., `[x*2 for x in data if x > 0]`).")
print("  🏆 Generally preferred in modern Python code for clarity and conciseness.")
print("="*60)

#=================PERFORMANCE COMPARISON=================
import time

def performance_test():
    """Compare performance of different approaches"""
    data = range(100000)
    
    # Using map
    start = time.time()
    result1 = list(map(lambda x: x**2, data))
    map_time = time.time() - start
    
    # Using list comprehension
    start = time.time()
    result2 = [x**2 for x in data]
    comp_time = time.time() - start
    
    print("PERFORMANCE COMPARISON (100,000 items):")
    print(f"Map + lambda:       {map_time:.4f} seconds")
    print(f"List comprehension: {comp_time:.4f} seconds")
    print(f"Winner: {'Map' if map_time < comp_time else 'Comprehension'} by {abs(map_time-comp_time)/min(map_time,comp_time)*100:.1f}%")

performance_test()
print("="*60)