# PYTHON DECORATORS - EXTENDING FUNCTION BEHAVIOR
# =================================================
# Decorators are a powerful and expressive feature in Python that allow you to dynamically
# add functionality to an existing function or class without modifying its source code.
# They are a form of "metaprogramming" and are heavily used in Python frameworks like Flask and Django.

# --- CORE CONCEPT: FUNCTIONS ARE FIRST-CLASS OBJECTS ---
# In Python, functions can be:
# 1. Assigned to variables.
# 2. Passed as arguments to other functions.
# 3. Returned from other functions.
# This is the foundation that makes decorators possible. A decorator is essentially a function
# that takes another function as input, adds some functionality (the "decoration"), and returns a new function.

# --- SYNTAX ---
# Decorators are typically applied using the `@` symbol followed by the decorator name,
# placed directly above the function definition. This is syntactic sugar for a more explicit function call.
#
# @my_decorator
# def my_function():
#     pass
#
# Is equivalent to:
# my_function = my_decorator(my_function)

import time
import functools # Import functools to use functools.wraps

# ================= EXAMPLE 1: A SIMPLE TIMER DECORATOR =================
print("--- Example 1: Function Timer ---")
print("="*60)

# This is our decorator function. It takes a function `func` as its argument.
def timer_decorator(func):
    # The `wrapper` function is what will replace the original function.
    # It can accept any number of positional (*args) and keyword (**kwargs) arguments,
    # making the decorator versatile and applicable to any function.
    @functools.wraps(func) # This is a helper decorator. It preserves the original function's metadata (like its name and docstring).
    def wrapper(*args, **kwargs):
        # 1. CODE TO EXECUTE *BEFORE* THE ORIGINAL FUNCTION
        print(f"Starting timer for '{func.__name__}'...")
        start_time = time.time()  # Record the start time

        # 2. CALL THE ORIGINAL FUNCTION
        # The result of the original function is captured.
        result = func(*args, **kwargs)

        # 3. CODE TO EXECUTE *AFTER* THE ORIGINAL FUNCTION
        end_time = time.time()  # Record the end time
        execution_time = end_time - start_time
        print(f"'{func.__name__}' finished in {execution_time:.6f} seconds.")
        
        # 4. RETURN THE ORIGINAL FUNCTION'S RESULT
        return result
    
    # The decorator returns the newly defined wrapper function.
    return wrapper

# --- APPLYING THE DECORATOR ---
# The `@timer_decorator` syntax automatically applies our decorator to the `sum_numbers` function.
@timer_decorator
def sum_numbers(n):
    """
    A simple function to calculate the sum of numbers from 1 to n.
    Its execution time will be measured by the decorator.
    """
    print("   (Inside sum_numbers: Calculating sum...)")
    return sum(range(1, n + 1))

# --- CALLING THE DECORATED FUNCTION ---
# When we call `sum_numbers`, we are actually calling the `wrapper` function returned by `timer_decorator`.
result = sum_numbers(1000000)
print(f"Sum result: {result}")
print(f"Original function name: {sum_numbers.__name__}") # Thanks to @functools.wraps, this is 'sum_numbers', not 'wrapper'
print(f"Original docstring: {sum_numbers.__doc__}")
print("="*60)


# ================= EXAMPLE 2: AN AUTHORIZATION DECORATOR =================
print("\n--- Example 2: Access Control / Authorization ---")
print("="*60)

# This decorator checks for a specific condition (user role) before executing the function.
def authorize(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Check if 'role' is provided as a keyword argument. Default to 'guest' if not.
        role = kwargs.get('role', 'guest')
        
        # --- AUTHORIZATION LOGIC ---
        if role == 'admin':
            # If authorized, call the original function and return its result.
            print(f"Authorization successful for role: '{role}'. Executing function.")
            return func(*args, **kwargs)
        else:
            # If not authorized, block execution and return an informative message.
            print(f"🚫 Unauthorized access for role: '{role}'! Action blocked. 🚫")
            return None # Or raise an exception: raise PermissionError("Admin access required")
            
    return wrapper

@authorize
def delete_data(user_id, *, role='guest'): # Using a keyword-only argument for clarity
    """Deletes sensitive data. Requires 'admin' role."""
    print(f"✅ Data for user '{user_id}' deleted successfully!")

# --- ATTEMPTING TO USE THE DECORATED FUNCTION ---

# Case 1: Unauthorized user (default role is 'guest')
print("Attempting to delete data as a guest...")
delete_data(123) 
print("-" * 20)

# Case 2: Unauthorized user (explicitly 'user' role)
print("Attempting to delete data as a standard user...")
delete_data(456, role='user')
print("-" * 20)

# Case 3: Authorized user ('admin' role)
print("Attempting to delete data as an admin...")
delete_data(789, role='admin')

print("="*60)

# --- KEY TAKEAWAYS ---
# • DRY Principle: Decorators help you follow the "Don't Repeat Yourself" principle by abstracting common setup/teardown logic (like timing, logging, or auth checks).
# • Separation of Concerns: The core business logic of your function (e.g., `delete_data`) is kept separate from cross-cutting concerns (e.g., `authorize`).
# • Readability: Using `@decorator` is clean and clearly states that the function's behavior is being modified.
# • Reusability: A single decorator can be applied to many different functions.