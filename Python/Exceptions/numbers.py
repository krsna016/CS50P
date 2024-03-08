# # # Value Error : If the user enters a string instead of a number
# x = int(input("Enter a number : "))
# print(f"x is {x}")


# # # Fix:
# try:
#     x = int(input("Enter a number : "))
#     print(f"x is {x}")
# except ValueError:
#     print(f"This is not a integer value !!")


# # # Name Error : The variable x is not defined if the exception is raised
# try:
#     x = int(input("Enter a number : "))
# except ValueError:
#     print(f"This is not a integer value !!")
# print(f"x is {x}")


# # # Fix:
# try:
#     x = int(input("Enter a number : "))
# except ValueError:
#     print(f"This is not a integer value !!")
# else:
#     print(f"x is {x}")


# # # Improving the code:
while True:
    try:
        x = int(input("Enter a number : "))
        break
    except ValueError:
        print(f"Please enter a Integer Value !!")
        continue
print(f"x is {x}")