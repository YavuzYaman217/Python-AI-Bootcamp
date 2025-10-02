# PYTHON SYNTAX BASICS - COMPLETE BEGINNER'S GUIDE
# =================================================
# This file covers fundamental Python concepts every beginner should know
# Topics: Variables, Data Types, Collections (Lists, Tuples, Dictionaries), and Control Flow

#=================VARIABLES AND BASIC DATA TYPES=================
# Variables are containers that store data values
# Python automatically determines the data type based on the value assigned

x = 10              # Integer (whole number)
y = 3.14            # Float (decimal number)  
greeting = "Hello, World!"  # String (text)

print("="*60)
print("BASIC VARIABLES:")
print(f"x = {x} (type: {type(x).__name__})")
print(f"y = {y} (type: {type(y).__name__})")
print(f"greeting = '{greeting}' (type: {type(greeting).__name__})")
print("="*60)
#=================BOOLEAN AND COLLECTIONS=================
is_active = True    # Boolean (True/False values)

# LISTS: Ordered, changeable collections that allow duplicate values
my_list = [1, "Hello", x, 3.12, False]  # Can contain different data types
print("LISTS:")
print(f"my_list = {my_list}")
print(f"Type: {type(my_list).__name__}, Length: {len(my_list)}")
print(f"First item: {my_list[0]}, Last item: {my_list[-1]}")  # Indexing examples
print("="*60)
# TUPLES: Ordered, unchangeable collections (immutable)
my_tuple = (1, "Hello", x, 3.12, False)
print("TUPLES:")
print(f"my_tuple = {my_tuple}")
print(f"Type: {type(my_tuple).__name__}, Length: {len(my_tuple)}")
# my_tuple[0] = 100  # ❌ This would raise an error - tuples cannot be changed!
print("Note: Tuples are immutable - you cannot change their contents after creation")
print("="*60)

# DICTIONARIES: Unordered collections of key-value pairs (like a real dictionary)
my_dict = {"Name": "Yavuz", "Age": 25, "City": "Istanbul"}
print("DICTIONARIES:")
print(f"my_dict = {my_dict}")
print(f"Accessing values: Name = {my_dict['Name']}, Age = {my_dict['Age']}")
print(f"My name is {my_dict['Name']} and I'm {my_dict['Age']} years old and live in {my_dict['City']}")
print("="*60)

#=================MODIFYING COLLECTIONS=================
print("MODIFYING COLLECTIONS:")

# Lists are MUTABLE - you can change, add, or remove items
print("Before modification:")
print(f"my_list = {my_list}")
print(f"my_dict = {my_dict}")

my_list.append("New Item")      # Add item to end of list
my_dict["Country"] = "Turkey"   # Add new key-value pair to dictionary

print("\nAfter modification:")
print(f"my_list = {my_list}")   # Now has "New Item" at the end
print(f"my_dict = {my_dict}")   # Now includes "Country": "Turkey"

print("\nKEY DIFFERENCES:")
print("• Lists: Use numbers as indices [0, 1, 2, ...]")
print("• Dictionaries: Use keys as indices ['Name', 'Age', 'City']")
print("• Tuples: Cannot be modified after creation")
print("="*60)

#=================CONDITIONAL STATEMENTS (IF/ELIF/ELSE)=================
print("CONDITIONAL STATEMENTS:")
my_value = 2

if my_value == 1:                    # First condition to check
    print("Value is one")
elif my_value == 2:                  # Second condition (only checked if first is False)
    print("Value is two")
else:                                # Executed if all above conditions are False
    print("Value is something else")

# HOW IT WORKS:
# 1. Python checks: Is my_value == 1? → False (2 ≠ 1)
# 2. Python checks: Is my_value == 2? → True (2 == 2) ✓
# 3. Executes: print("Value is two")
# 4. Skips the 'else' block since a condition was already True

print("\nCONDITIONAL OPERATORS:")
print("== : Equal to")
print("!= : Not equal to") 
print(">  : Greater than")
print("<  : Less than")
print(">= : Greater than or equal to")
print("<= : Less than or equal to")
print("="*60)

#=================SUMMARY OF CONCEPTS COVERED=================
print("CONCEPTS LEARNED:")
print("✓ Variables and basic data types (int, float, string, bool)")
print("✓ Lists: Ordered, mutable collections [item1, item2, ...]")
print("✓ Tuples: Ordered, immutable collections (item1, item2, ...)")
print("✓ Dictionaries: Key-value pairs {'key': 'value', ...}")
print("✓ Conditional statements: if/elif/else for decision making")
print("✓ Collection modification: append(), adding dictionary keys")
print("✓ Built-in functions: len(), type(), print()")
print("="*60)





