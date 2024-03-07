"""
Pseudocode:
Step 1: Start
Step 2 : Say hello to the world
Step 3: Ask for user's name
Step 4 : Ask for user's age
Step 5: Print the user's name
Step 6: End
"""

# Code:

# Say hello to the world:
print("Hello World!")

# Dynamic input:

# Ask for user's name:
name = input("What's your name? : ")

# Ask for user's age:
age = input("What's your age? : ")

# Print the user's name:
print("Hello,")
print(name)
print("!")

# Or

# We can use the + operator to concatenate strings, we can even concatenate multiple strings
print("Hello, " + name + "!")

# Or

print("Hello, ", end="")
print(name, end="")
print("!")

# Or

# Here we can pass multiple arguments to the print function and they are automatically separated by a space
print("Hello,", name, age, "!", sep="???")
