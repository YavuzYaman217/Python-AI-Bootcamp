# OBJECT-ORIENTED PROGRAMMING (OOP) IN PYTHON - A BEGINNER'S GUIDE
# =================================================================
# OOP is a programming paradigm that structures code around "objects", which can contain both data (attributes) and code (methods).
# Think of a "class" as a blueprint and an "object" as a specific instance built from that blueprint.

#=================EXAMPLE 1: DEFINING A BASIC CLASS AND CREATING OBJECTS=================
class Car:
    """
    This class serves as a blueprint for creating car objects.
    """
    
    # CLASS ATTRIBUTE: This is a property shared by ALL instances (objects) of the Car class.
    # It's defined directly within the class.
    wheels = 4
    
    def __init__(self, model: str, year: int, color: str):
        """
        The constructor method, also known as the initializer.
        It's a special method that is automatically called when you create a new object from this class.
        The `self` parameter refers to the specific instance of the object being created.
        """
        # INSTANCE ATTRIBUTES: These are unique to each object created from the class.
        # They are defined inside the `__init__` method and are prefixed with `self`.
        self.model = model  # Each car will have its own model.
        self.year = year    # Each car will have its own manufacturing year.
        self.color = color  # Each car will have its own color.
        
    def display_info(self):
        """
        This is an instance method. It's a function defined inside a class that can be called on any object of the class.
        It automatically receives the object instance as its first argument (`self`).
        """
        # This method prints the details of a specific car instance.
        print(f"🚗 Model: {self.model}, Year: {self.year}, Color: {self.color}, Wheels: {self.wheels}")

print("CREATING CAR OBJECTS (INSTANCES):")
print("="*60)
# Creating objects (also called instances) from the Car class blueprint.
my_car = Car("Toyota Camry", 2021, "Red")      # This creates the first Car object.
your_car = Car("Honda Civic", 2019, "Blue")    # This creates a second, distinct Car object.

# Each object has its own unique data but follows the structure defined by the class.
print("My car's information:")
my_car.display_info()  # Calling the method on the `my_car` object.

print("Your car's information:")
your_car.display_info() # Calling the method on the `your_car` object.

# Accessing attributes directly.
print(f"\nBoth cars have {Car.wheels} wheels (this is a class attribute).")
print(f"My car's model is: {my_car.model} (this is an instance attribute).")
print(f"Your car's model is: {your_car.model} (this is an instance attribute).")
print("="*60)

#=================EXAMPLE 2: ENCAPSULATION - CONTROLLING ACCESS TO DATA=================
# Encapsulation is the concept of bundling data (attributes) and the methods that operate on that data into a single unit (a class).
# It also involves restricting direct access to some of an object's components, which is a key principle for data hiding.

class MyClass:
    """
    This class demonstrates the different access levels for variables in Python.
    """
    def __init__(self):
        self.public_var = "I'm public - accessible from anywhere."
        self._protected_var = "I'm protected - intended for internal use or by subclasses (by convention)." # Single underscore prefix
        self.__private_var = "I'm private - access is restricted from outside the class." # Double underscore prefix
        
    def get_private_var(self):
        """A public method to provide controlled access to the private variable."""
        return self.__private_var
    
    def display_all_vars(self):
        """A method to display all variables from within the class."""
        print(f"Inside the class: Public: {self.public_var}")
        print(f"Inside the class: Protected: {self._protected_var}")
        print(f"Inside the class: Private: {self.__private_var}")

print("ENCAPSULATION DEMONSTRATION:")
obj = MyClass()

# PUBLIC ACCESS: ✅ You can directly access public variables.
print(f"✅ Accessing public variable: {obj.public_var}")

# PROTECTED ACCESS: ⚠️ You can still access it, but the underscore signals that you shouldn't do it directly.
print(f"⚠️ Accessing protected variable (by convention, should be avoided): {obj._protected_var}")

# PRIVATE ACCESS: ❌ Direct access is not possible due to name mangling.
# print(obj.__private_var)  # This line would raise an AttributeError.
# Instead, we use a "getter" method to access it safely.
print(f"✅ Accessing private variable via a public method: {obj.get_private_var()}")

print("\nWHY IS ENCAPSULATION USEFUL?")
print("• It protects the object's internal state from accidental or malicious modification.")
print("• It allows the class to enforce invariants and validate data.")
print("• It makes the code more modular, maintainable, and secure.")
print("="*60)

#=================EXAMPLE 3: A PRACTICAL APPLICATION - BANK ACCOUNT=================
class Account:
    """
    A more realistic example of OOP, modeling a bank account.
    This class demonstrates encapsulation, data validation, and controlled access to attributes.
    """
    
    def __init__(self, account_number: int, owner: str, balance: float = 0.0):
        """Initializes a new bank account."""
        # All attributes are made private to ensure data integrity and security.
        self.__account_number = account_number
        self.__owner = owner
        self.__balance = balance
        
        print(f"🏦 New account created for {owner} with an initial balance of ${balance:.2f}")
        
    def deposit(self, amount: float):
        """Adds money to the account, but only if the amount is valid."""
        if amount > 0:
            self.__balance += amount
            print(f"💰 Deposit successful: ${amount:.2f}. New balance: ${self.__balance:.2f}")
        else:
            print("❌ Invalid operation: Deposit amount must be positive.")
            
    def withdraw(self, amount: float):
        """Removes money from the account, with checks for sufficient funds and valid amount."""
        if amount <= 0:
            print("❌ Invalid operation: Withdrawal amount must be positive.")
        elif amount > self.__balance:
            print("❌ Transaction failed: Insufficient funds.")
        else:
            self.__balance -= amount
            print(f"💸 Withdrawal successful: ${amount:.2f}. New balance: ${self.__balance:.2f}")
            
    def display_balance(self):
        """A public method to safely display the current account balance."""
        print(f"💳 Current account balance: ${self.__balance:.2f}")
        
    def get_account_info(self):
        """
        A safe method to retrieve account information.
        It returns a dictionary with formatted data, hiding sensitive details.
        """
        return {
            "owner": self.__owner,
            "account_number": f"****{str(self.__account_number)[-4:]}",  # Only show the last 4 digits
            "balance": f"${self.__balance:.2f}"
        }

# --- SIMULATING BANK ACCOUNT OPERATIONS ---
print("BANK ACCOUNT SIMULATION:")
print("="*60)

# Create a new account instance.
acc1 = Account(1234567890, "Yavuz", 1000.0)

# Perform some valid transactions.
acc1.deposit(500.50)
acc1.withdraw(200.25)
acc1.display_balance()

# Attempt some invalid operations.
print("\n--- Testing Invalid Operations ---")
acc1.deposit(-50)       # Trying to deposit a negative amount.
acc1.withdraw(2000)     # Trying to withdraw more money than available.

# Safely retrieve and display account information.
print("\n--- Retrieving Account Summary ---")
account_summary = acc1.get_account_info()
print(f"Account Summary: {account_summary}")

print("="*60)

#=================SUMMARY OF OOP PRINCIPLES COVERED=================
print("🎯 KEY OOP CONCEPTS DEMONSTRATED:")
print("✓ CLASSES: The blueprint for creating objects (e.g., `Car`, `Account`).")
print("✓ OBJECTS: The actual instances created from a class (e.g., `my_car`, `acc1`).")
print("✓ ENCAPSULATION: Hiding internal data (e.g., `__balance`) and providing public methods (`deposit`, `withdraw`) to interact with it.")
print("✓ METHODS: Functions defined within a class that operate on an object's data.")
print("✓ CONSTRUCTOR (`__init__`): The special method used to initialize an object's state when it's created.")
print("✓ DATA VALIDATION: Ensuring that the data being assigned to attributes is valid (e.g., checking for positive deposit amounts).")
print("✓ ABSTRACTION: Hiding complex implementation details and exposing only the necessary functionalities (e.g., you don't need to know how `deposit` works internally, just that it adds money).")
print("="*60)