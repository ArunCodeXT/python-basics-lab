# Day 2: Variables and Data Types
# Variables
name = "Arun"
age = 21
height = 5.9
is_student = True

# Print using f-string
print(f"My name is {name}, I am {age} years old, and my height is {height} feet.")

# Type checking
print("Type of name:", type(name))
print("Type of age:", type(age))
print("Type of height:", type(height))
print("Type of is_student:", type(is_student))

# Updating variables
age = age + 1
print(f"Next year I will be {age} years old.")

# Mutability vs Immutability
my_list = [1, 2, 3]
my_list.append(4)   # list is mutable
print("Updated list:", my_list)

my_str = "Python"
# Strings are immutable → this creates a new string
new_str = my_str + " is fun"
print("New string:", new_str)