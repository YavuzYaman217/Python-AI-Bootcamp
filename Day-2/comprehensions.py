# LIST COMPREHENSIONS - POWERFUL PYTHON FEATURE
# ==============================================
# List comprehensions provide a concise, readable way to create lists
# They're more efficient and "Pythonic" than traditional for loops for list creation
# 
# SYNTAX: [expression for item in iterable if condition]
# 
# Benefits:
# • More readable and compact code
# • Often faster than equivalent for loops  
# • Can include filtering with conditions
# • Works with any iterable (lists, strings, ranges, etc.)

#=================EXAMPLE 1: BASIC LIST COMPREHENSION=================
print("CREATING SQUARES: Traditional vs Comprehension")
print("="*60)

# TRADITIONAL WAY: Using a for loop (verbose, more lines)
squares_traditional = []
for i in range(10):
    squares_traditional.append(i**2)
print(f"Traditional method: {squares_traditional}")

# LIST COMPREHENSION WAY: One line, more readable
squares_comprehension = [i**2 for i in range(10)]
print(f"List comprehension: {squares_comprehension}")

# BREAKDOWN OF COMPREHENSION SYNTAX:
# [i**2 for i in range(10)]
#  ^^^^     ^^^^^^^^^^^^^^^
#  │        └── Iterable: where to get values from
#  └── Expression: what to do with each value

print(f"\nResult: {squares_traditional == squares_comprehension} (both methods produce identical results)")
print("="*60)


#=================EXAMPLE 2: COMPREHENSIONS WITH CONDITIONS=================
print("FILTERING WITH CONDITIONS:")

# Only even numbers, then square them
even_squares = [i**2 for i in range(10) if i % 2 == 0]
print(f"Even squares: {even_squares}")

# BREAKDOWN: [i**2 for i in range(10) if i % 2 == 0]
#            ^^^^                      ^^^^^^^^^^^^^
#            │                         └── Condition: only process if true
#            └── Expression: applied only to items that pass the condition

# Traditional equivalent:
traditional_even_squares = []
for i in range(10):
    if i % 2 == 0:  # Only even numbers
        traditional_even_squares.append(i**2)
print(f"Traditional equivalent: {traditional_even_squares}")

# Another example: Numbers divisible by 3
multiples_of_3 = [n for n in range(20) if n % 3 == 0]
print(f"Multiples of 3 (0-19): {multiples_of_3}")

# Complex condition example
filtered_numbers = [x for x in range(1, 21) if x % 2 == 0 and x > 10]
print(f"Even numbers greater than 10: {filtered_numbers}")
print("="*60)


#=================EXAMPLE 3: DICTIONARY COMPREHENSIONS=================
print("DICTIONARY COMPREHENSIONS:")

# Create a dictionary mapping numbers to their squares
square_dict = {i: i**2 for i in range(10)}
print(f"Number → Square mapping: {square_dict}")

# SYNTAX: {key_expression: value_expression for item in iterable}
#         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#         │                               └── Same as list comprehension
#         └── Key: Value pairs instead of just values

# More examples:
word_lengths = {word: len(word) for word in ["apple", "banana", "cherry"]}
print(f"Word lengths: {word_lengths}")

# With conditions
even_squares_dict = {i: i**2 for i in range(10) if i % 2 == 0}
print(f"Even numbers and their squares: {even_squares_dict}")
print("="*60)


#=================EXAMPLE 4: REAL-WORLD APPLICATION=================
print("PRACTICAL EXAMPLE: Text Processing")

words = ["apple", "is", "banana", "cat", "dog", "elephant", "programming", "hi"]

# Filter words with more than 5 letters
long_words = [word for word in words if len(word) > 5]
print(f"Long words (>5 letters): {long_words}")

# Create dictionary of long words and their lengths
word_analysis = {word: len(word) for word in words if len(word) > 5}
print(f"Long word analysis: {word_analysis}")

# Multiple processing: uppercase long words
long_words_upper = [word.upper() for word in words if len(word) > 5]
print(f"Long words (uppercase): {long_words_upper}")

# Complex example: first letter of words starting with vowels
vowel_words = [word[0].upper() + word[1:] for word in words if word[0].lower() in 'aeiou']
print(f"Words starting with vowels (capitalized): {vowel_words}")
print("="*60)

#=================SET COMPREHENSIONS=================
print("BONUS: SET COMPREHENSIONS")
# Sets automatically remove duplicates and are unordered
unique_lengths = {len(word) for word in words}
print(f"Unique word lengths: {unique_lengths}")

# Remember: sets are unordered, so the display order may vary!
print("Note: Sets are unordered collections, so order may vary between runs")
print("="*60)

#=================PERFORMANCE COMPARISON=================
import time

def time_comparison():
    """Compare performance of traditional loops vs comprehensions"""
    n = 100000
    
    # Traditional loop
    start = time.time()
    traditional = []
    for i in range(n):
        if i % 2 == 0:
            traditional.append(i**2)
    traditional_time = time.time() - start
    
    # List comprehension  
    start = time.time()
    comprehension = [i**2 for i in range(n) if i % 2 == 0]
    comprehension_time = time.time() - start
    
    print("PERFORMANCE COMPARISON (100,000 items):")
    print(f"Traditional loop: {traditional_time:.4f} seconds")
    print(f"List comprehension: {comprehension_time:.4f} seconds") 
    print(f"Comprehension is {traditional_time/comprehension_time:.1f}x faster!")

time_comparison()
print("="*60)

#=================COMPREHENSION BEST PRACTICES=================
print("📚 COMPREHENSION BEST PRACTICES:")
print("✅ Use for simple transformations and filtering")
print("✅ Keep expressions readable - avoid overly complex logic")
print("✅ Prefer comprehensions over map() and filter() for readability")
print("❌ Don't use for complex logic - use regular loops instead")
print("❌ Avoid nested comprehensions that are hard to read")
print("❌ Don't use just for side effects - use regular loops")
print("="*60)