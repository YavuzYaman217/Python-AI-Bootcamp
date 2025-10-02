# PYTHON FUNCTIONS - COMPLETE GUIDE
# ==================================
# Functions are reusable blocks of code that perform specific tasks
# They help organize code, avoid repetition, and make programs more readable

#=================EXAMPLE 1: BASIC FUNCTION=================
# A simple function that takes one parameter and performs an action
def greet(name):  # Function definition: 'def' keyword + function_name(parameters):
    """This function prints a greeting message"""  # Docstring (optional but recommended)
    print(f"Hello, {name}!")  # Function body - what the function does

# Function call: using the function by passing an argument
greet("Yavuz")  # Output: Hello, Yavuz!

# KEY CONCEPTS:
# - 'name' is a PARAMETER (placeholder in function definition)
# - "Yavuz" is an ARGUMENT (actual value passed when calling)
print("="*60)

#=================EXAMPLE 2: FUNCTION WITH RETURN VALUE=================
# Functions can return values using the 'return' keyword
def add(a, b) -> int:  # '-> int' is a TYPE HINT (tells us this function returns an integer)
    """
    This function adds two numbers and returns the result
    
    Parameters:
    a (int): First number
    b (int): Second number
    
    Returns:
    int: Sum of a and b
    """
    return a + b  # 'return' sends a value back to whoever called the function

# Capture the returned value in a variable
result = add(5, 3)  # The function calculates 5+3 and returns 8
print(f"5 + 3 = {result}")  # Output: 5 + 3 = 8

# IMPORTANT DIFFERENCE:
# - greet() function: performs an action (printing) but returns nothing
# - add() function: performs calculation AND returns a value we can use
print("="*60)

#=================EXAMPLE 3: DEFAULT PARAMETERS=================
# You can give parameters default values - if no argument is provided, the default is used
def power(base: int, exponent: int = 2) -> int:  # exponent has default value of 2
    """
    Calculate base raised to the power of exponent
    
    Parameters:
    base (int): The base number
    exponent (int, optional): The exponent. Defaults to 2 (square).
    
    Returns:
    int: Result of base^exponent
    """
    return base ** exponent  # ** is the power operator in Python

# Using the function with different numbers of arguments:
print(f"3^2 = {power(3)}")        # Only base provided, uses default exponent=2 → 3²=9
print(f"3^3 = {power(3, 3)}")     # Both arguments provided, overrides default → 3³=27
print(f"2^4 = {power(2, 4)}")     # Another example → 2⁴=16

# WHY USE DEFAULT PARAMETERS?
# - Makes functions more flexible and easier to use
# - Common use case (like squaring) becomes simpler
# - Still allows customization when needed
print("="*60)

#=================ADDITIONAL CONCEPTS=================
# More advanced function concepts you'll learn later:
# - *args: Variable number of arguments
# - **kwargs: Keyword arguments  
# - Lambda functions: One-line anonymous functions
# - Recursive functions: Functions that call themselves
# - Scope: Local vs global variables
