"""
PROBLEM: Non-Pythonic List and Dictionary Operations
=====================================================
Python provides powerful comprehension syntax for creating lists and dictionaries.
Using traditional loops with append() and update() is verbose, slower, and not idiomatic.

ISSUE DEMONSTRATION (Commented Code Below):
1. Using a for loop with append() to filter a list - inefficient and verbose
2. Using a for loop with dict.update() to build a dictionary - unnecessarily complex

# list_and_dict_errors.py

students = [
    {"name": "Ece", "score": 85},
    {"name": "Ali", "score": 62},
    {"name": "Burak", "score": 78},
    {"name": "Can", "score": 55},
    {"name": "Deniz", "score": 90}
]

def filter_and_map_students(data):
    passed_students = []
    
    # Error 1: This loop is not Pythonic and unnecessary
    # Using traditional loop to filter - verbose and slow
    for student in data:
        if student["score"] >= 70:
            passed_students.append(student)

    # Error 2: Dictionary creation logic is inefficient
    # Using loop with update() is slower than dict comprehension
    results_dict = {}
    for student in passed_students:
        results_dict.update({student["name"]: student["score"]})
    
    return results_dict

final_results = filter_and_map_students(students)
print(final_results)
# Expected Output: {'Ece': 85, 'Burak': 78, 'Deniz': 90}
"""

# SOLUTION: Using List Comprehension and Dictionary Comprehension
# ================================================================
# Python comprehensions are more readable, faster, and follow Python best practices
# They express the intent clearly in a single line

students = [
    {"name": "Ece", "score": 85},
    {"name": "Ali", "score": 62},
    {"name": "Burak", "score": 78},
    {"name": "Can", "score": 55},
    {"name": "Deniz", "score": 90}
]

def filter_and_map_students(data):
    """
    Filters students who passed (score > 70) and creates a dictionary mapping names to scores.
    
    Args:
        data: List of dictionaries containing student information
        
    Returns:
        Dictionary with student names as keys and scores as values
    """
    # Fix 1: List comprehension - more Pythonic, concise, and faster
    # Filters students with score > 70 in a single, readable line
    passed_students = [user for user in data if user['score'] > 70] 

    # Fix 2: Dictionary comprehension - elegant and efficient
    # Creates a dictionary directly without intermediate steps
    results_dict = {student['name']: student['score'] for student in passed_students}
    
    return results_dict

# Execute the function and print results
final_results = filter_and_map_students(students)
print(final_results)  # Output: {'Ece': 85, 'Burak': 78, 'Deniz': 90}