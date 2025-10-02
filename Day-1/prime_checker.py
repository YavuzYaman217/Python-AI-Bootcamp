# PRIME NUMBER CHECKER - A PRACTICAL EXAMPLE COMBINING LOOPS AND CONDITIONALS
# =========================================================================
# This program demonstrates a common and practical use of loops and conditional statements (`if`, `else`)
# to solve a mathematical problem: determining if a given number is a prime number.

# --- WHAT IS A PRIME NUMBER? ---
# A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
# In other words, it cannot be formed by multiplying two smaller natural numbers.
#
# - Examples of prime numbers: 2, 3, 5, 7, 11, 13, 17, 19...
# - Examples of non-prime (composite) numbers: 4 (2*2), 6 (2*3), 8 (2*4), 9 (3*3)...
#
# Key facts:
# - The number 1 is not a prime number by definition.
# - The number 2 is the only even prime number. All other even numbers are divisible by 2.

# --- GETTING USER INPUT ---
print("--- PRIME NUMBER CHECKER ---")
print("="*40)
# We ask the user to enter an integer and store it in the `number` variable.
try:
    number_to_check = int(input("Enter a whole number to check if it's prime: "))
except ValueError:
    print("Invalid input. Please enter a valid integer.")
    exit() # Exit the program if the input is not a number.

def is_prime(num: int) -> bool:
    """
    Checks if a given number is prime using an efficient algorithm.
    
    Args:
        num (int): The integer to check.
        
    Returns:
        bool: True if the number is prime, False otherwise.
    """
    
    # STEP 1: Handle edge cases first for efficiency.
    # Prime numbers must be greater than 1.
    if num <= 1:
        print(f"Info: {num} is not a prime number because primes must be greater than 1.")
        return False
    
    # STEP 2: The main logic for checking primality.
    # We check for divisors from 2 up to the square root of the number.
    # This is a common optimization: if a number `n` has a divisor larger than its square root,
    # it must also have a corresponding divisor smaller than its square root.
    # So, we only need to check for divisors up to `sqrt(n)`.
    # Example: To check if 100 is prime, we only need to check up to sqrt(100) = 10.
    # If we find 2 is a divisor (100/2 = 50), we don't need to check for 50.
    
    # We iterate from 2 up to `int(num**0.5) + 1`.
    # `num**0.5` calculates the square root. `int()` converts it to an integer. `+1` ensures the upper bound is included.
    for i in range(2, int(num**0.5) + 1):
        # The modulo operator (`%`) gives the remainder of a division.
        # If the remainder is 0, it means `i` is a divisor of `num`.
        if num % i == 0:
            # If we find even one divisor, we know the number is not prime.
            # We can immediately return False and stop the loop.
            print(f"Info: {num} is not prime because it is divisible by {i} (e.g., {i} * {num // i} = {num}).")
            return False
    
    # If the loop completes without finding any divisors, the number must be prime.
    return True

# --- MAIN PROGRAM EXECUTION ---
print("="*40)
# Call the `is_prime` function with the user's number and check the returned boolean value.
if is_prime(number_to_check):
    print(f"✅ Result: {number_to_check} is a PRIME number!")
else:
    print(f"❌ Result: {number_to_check} is NOT a prime number.")

print("="*40)

# --- ALGORITHM EFFICIENCY INSIGHTS ---
print("\n--- How the Algorithm Works (Efficiency) ---")
# A naive approach would be to check for divisors from 2 all the way up to `num - 1`.
# Our optimized approach is much faster for large numbers.
limit = int(number_to_check**0.5)
print(f"• For the number {number_to_check}, we only need to check for divisors from 2 up to {limit}.")
print(f"• A less efficient method would check all the way up to {number_to_check - 1}.")

if number_to_check > 100:
    naive_checks = number_to_check - 2
    optimized_checks = max(1, limit - 1)
    if optimized_checks > 0:
        efficiency_gain = naive_checks / optimized_checks
        print(f"• This optimization makes the check approximately {efficiency_gain:.1f} times faster!")

# --- SUGGESTED NUMBERS TO TRY ---
print("\n--- Try Checking These Numbers ---")
print("• 7 (a small prime)")
print("• 97 (a larger prime)")
print("• 100 (a non-prime/composite number)")
print("• 899 (a non-prime with less obvious factors: 29 * 31)")
