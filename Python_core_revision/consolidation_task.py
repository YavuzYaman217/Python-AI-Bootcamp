# CONSOLIDATION TASK: USER DATA PROCESSING
# ===========================================
# This program demonstrates several key Python concepts:
# 1. List comprehensions with filtering
# 2. Dictionary comprehensions  
# 3. String manipulation (split(), lower())
# 4. Functions with type hints
# 5. Data filtering and processing

# Sample dataset: List of dictionaries representing user data
# Each user has: name, age, status, and join_year
raw_users = [
    {"name": "Alice Smith", "age": 30, "status": "active", "join_year": 2020},
    {"name": "Bob Johnson", "age": 17, "status": "pending", "join_year": 2024},  # Under 18, pending
    {"name": "Charlie Brown", "age": 45, "status": "active", "join_year": 2019},
    {"name": "David Wilson", "age": 22, "status": "INACTIVE", "join_year": 2023},  # Inactive (note: uppercase)
    {"name": "Eve Davis", "age": 16, "status": "active", "join_year": 2025},  # Under 18
]

# STEP 1: Filter eligible users using LIST COMPREHENSION
# Requirements: age >= 18 AND status = 'active' (case-insensitive)
# Extract only first names using split()[0]
eligible_users = [user['name'].split()[0] for user in raw_users
                  if user['age'] >= 18 and user['status'].lower() == 'active']

print("Eligible users (first names only):", eligible_users)
# Expected output: ['Alice', 'Charlie'] 
# Bob: age 17 (too young), David: inactive, Eve: age 16 (too young)
print("="*50)


# STEP 2: Define a function to calculate membership seniority
# Type hints: parameter 'year' is int, return value is int
def calculate_seniority(year: int) -> int:
    """Calculate how many years a user has been a member"""
    current_year = 2025
    return current_year - year
# STEP 3: Create seniority dictionary using DICTIONARY COMPREHENSION
# Only include users whose first names are in the eligible_users list
# Key: full name, Value: years of membership
seniority_dict = {user['name']: calculate_seniority(user['join_year']) 
                  for user in raw_users 
                  if user['name'].split()[0] in eligible_users}

print("Seniority dictionary:", seniority_dict)
# Expected: {'Alice Smith': 5, 'Charlie Brown': 6}
print("="*50)

# STEP 4: Display results using dictionary iteration and f-strings
print("FINAL RESULTS:")
print("-" * 30)
for senior_user in seniority_dict:
    print(f"{senior_user} has been a member for {seniority_dict[senior_user]} years.")

# SUMMARY OF CONCEPTS DEMONSTRATED:
# ================================
# 1. LIST COMPREHENSION: Filtering and transforming data in one line
# 2. DICTIONARY COMPREHENSION: Creating key-value pairs with conditions
# 3. STRING METHODS: split(), lower() for text processing
# 4. FUNCTION DEFINITION: With type hints and docstring
# 5. CONDITIONAL FILTERING: Multiple conditions with 'and'
# 6. F-STRING FORMATTING: Modern string interpolation
# 7. DICTIONARY ITERATION: Looping through keys
# 8. DATA PROCESSING PIPELINE: Raw data → Filter → Transform → Display