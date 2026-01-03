# Day 4: Type Casting Examples

# Input from user
num_str = input("Enter a number: ")  # string input

# Safe casting to int
try:
    num = int(num_str)
    print(f"Your number multiplied by 2: {num * 2}")
except ValueError:
    print("Error: You did not enter a valid integer!")

# Float example
float_input = input("Enter a decimal number: ")
try:
    f = float(float_input)
    print(f"Half of your number: {f / 2}")
except ValueError:
    print("Error: Not a valid float!")

# Boolean example
text = input("Enter any text to check truthiness: ")
print(f"Truthiness of '{text}': {bool(text)}")
