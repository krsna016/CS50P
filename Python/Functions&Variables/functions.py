# """
# 1. Define a function called hello that takes a name as an argument and prints "Hello, [name]!" to the console.
# 2. def is a keyword that tells Python you're about to define a function.
# 3. hello is the name of the function.
# 4. name is the argument the function takes.
# """
# # The defination of function should be before the call of function or at top of the file.
# # We can also give default values to the arguments of a function.
# def hello(to="World"):
#     print(f"Hello, {to}!")
# name = input("What's your name? : ")
# hello(name)
# hello()


# In this way we can put function even at end of the file and call it.
# Using main is a good practice to keep the code clean and readable.
def main():
    name = input("What's your name? : ")
    hello(name);


def hello(to="World"):
    print(f"Hello, {to}!")

main()
