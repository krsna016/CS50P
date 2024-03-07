# Ask user for the name: (returns string)
name = input("What's your name? : ")

print("\n--- String Operations ---")

# Remove white spaces and capitalize the string: (returns string)
print("Stripped and Capitalized String:", name.strip().capitalize())

# Remove white spaces from the string: (returns string)
print("Stripped String:", name.strip())

# Remove white spaces from the left side of the string: (returns string)
print("Left Stripped String:", name.lstrip())

# Remove white spaces from the right side of the string: (returns string)
print("Right Stripped String:", name.rstrip())

# Capitalize the string: (returns string)
print("Capitalized String:", name.capitalize())

# Convert the string to upper case: (returns string)
print("Uppercase String:", name.upper())

# Convert the string to lower case: (returns string)
print("Lowercase String:", name.lower())

# Replace the string: (returns string)
print("Replaced String:", name.replace("J", "K"))

# Split the string: (returns list)
print("Split String:", name.split(" "))

print("\n--- String Checks ---")

# Check if the string ends with a specific character: (returns boolean)
print("Ends with 'n':", name.endswith("n"))

# Check if the string starts with a specific character: (returns boolean)
print("Starts with 'J':", name.startswith("J"))

# Check the length of the string: (returns integer)
print("Length of String:", len(name))

# Check the index of a specific character: (returns integer)
print("Index of 'A':", name.index("A"))

# Count the number of a specific character: (returns integer)
print("Count of 'a':", name.count("a"))

# Check if the string is a digit: (returns boolean)
print("Is Digit:", name.isdigit())

# Check if the string is a number: (returns boolean)
print("Is Numeric:", name.isnumeric())

# Check if the string is a letter: (returns boolean)
print("Is Alpha:", name.isalpha())

# Check if the string is a letter or a number: (returns boolean)
print("Is Alphanumeric:", name.isalnum())

# Check if the string is a space: (returns boolean)
print("Is Space:", name.isspace())

# Check if the string is a title: (returns boolean)
print("Is Title:", name.istitle())

# Check if the string is a lowercase: (returns boolean)
print("Is Lower:", name.islower())

# Check if the string is a uppercase: (returns boolean)
print("Is Upper:", name.isupper())

# Check if the string is a printable: (returns boolean)
print("Is Printable:", name.isprintable())

# Check if the string is a decimal: (returns boolean)
print("Is Decimal:", name.isdecimal())

# Check if the string is a identifier: (returns boolean)
print("Is Identifier:", name.isidentifier())

# Check if the string is a ascii: (returns boolean)
print("Is ASCII:", name.isascii())

# Check if the string is a digit: (returns boolean)
print("Is Numeric:", name.isnumeric())
