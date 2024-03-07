# # Floats is a number with a decimal point
x = float(input("Enter a number : "))
y = float(input("Enter another number : "))
# print(f"{x}/{y} = {round(x / y, 7)}")
# print(f"{x}/{y} = {round(x / y)}")
# # The round function rounds the number to the nearest decimal place
# # The syntax is round(number [, decimal place])
# # We can also use the format function to format the number
print(f"{x}/{y} = {x / y:.2f}")
# # The syntax is {variable : format_specifier}


# # Printing number with comma separator
# x = int(input("Enter a number : "))
# y = int(input("Enter another number : "))
# print(f"{x} + {y} = {x + y:,}")
# # eg: 1000000 = 1,000,000
