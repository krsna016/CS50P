# # Type Casting - String(str) to Integer(int):
# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter another number: "))
# operation = input("Which operation would you like to perform? (+ or - or * or / or // or % or **) : ")
# if operation == '+':
#     print(f"{num1} + {num2} = {num1 + num2}")
# elif operation == '-':
#     print(f"{num1} - {num2} = {num1 - num2}")
# elif operation == '*':
#     print(f"{num1} * {num2} = {num1 * num2}")
# elif operation == '/':
#     print(f"{num1} / {num2} = {num1 / num2}")
# elif operation == '//':
#     print(f"{num1} // {num2} = {num1 // num2}")
# elif operation == '%':
#     print(f"{num1} % {num2} = {num1 % num2}")
# elif operation == '**':
#     print(f"{num1} ** {num2} = {num1 ** num2}")
# else:
#     print("Invalid operation")


# # We can even write the above code in a single line:
# # But it's not recommended as it's not readable.
# print("The sum is : ", int(input("Enter first num : ")) + int(input("Enter second num : ")))


# Using return statement:

def main():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    n = add(num1, num2);
    print(n)

def add(num1, num2):
    return num1 + num2

main()