# 5-2. More Conditional Tests

car = 'Bugati'

# • Tests for equality and inequality with strings
print("--- String Comparisons ---")
print("If car == 'Bugati'? I predict True")
print(car == 'Bugati') # True

print("\nIf car == 'audi'? I predict False")
print(car == 'audi') # False

# • Tests using the lower() method
print("\n--- .lower() Method Tests ---")
print("If car.lower() == 'bugati'? I predict True.") # Prediction corrected
print(car.lower() == 'bugati') # True (Added print for result)

print("\nIf car.lower() == 'BUGATI'? I predict False.") # Added new test
print(car.lower() == 'BUGATI') # False

age = 23

# • Numerical tests
print("\n--- Numerical Tests ---")
print("If age == 23? I predict True")
print(age == 23) # True

print("\nIf age >= 20? I predict True")
print(age >= 20) # True

print("\nIf age <= 30? I predict True.") # Prediction corrected, as 23 <= 30 is True
print(age <= 30) # True (Added print for result)

print("\nIf age < 20? I predict False.") # Added new test for False
print(age < 20) # False

# • Tests using the and keyword and the or keyword
print("\n--- 'and' and 'or' Keyword Tests ---")
print("If age >= 20 and age <= 30? I predict True")
print(age >= 20 and age <= 30) # True

print("\nIf age > 25 and age < 30? I predict False.") # Added new test for False
print(age > 25 and age < 30) # False

print("\nIf age >= 20 or age <= 20? I predict True.") # Prediction corrected
print(age >= 20 or age <= 20) # True

print("\nIf age < 10 or age > 50? I predict False.") # Added new test for False
print(age < 10 or age > 50) # False


names = ['shariar', 'hasan', 'shanto'] # Changed variable name from 'list' to 'names'

# • Test whether an item is in a list
print("\n--- 'in' List Tests ---")
print("Is 'jack' in names? I predict False.") # Added clear question
print('jack' in names) # False (Added print for result)

print("\nIs 'shariar' in names? I predict True.") # Added clear question
print('shariar' in names) # True (Added print for result)

# • Test whether an item is not in a list
print("\n--- 'not in' List Tests ---")
print("Is 'zaman' not in names? I predict True.") # Added 'not in' test
print('zaman' not in names) # True

print("\nIs 'hasan' not in names? I predict False.") # Added 'not in' test
print('hasan' not in names) # False