# name = input("Enter your name: ")
# if name == "Alice":
#     print("Hi, Alice")
# elif name == "Bob":
#     print("Hi, Bob")
# else:
#     print("Hi, stranger")

# Also:

# There is no default case in match statements. If you want to match any value that doesn't match the other cases, you can use _ as a wildcard.
name = input("Enter your name: ")
match name:
    # We use | to separate multiple patterns in a single case
    case "Alice" | "Ram" | "Shyam" | "Hari" | "Sita" | "Gita" | "Rita" | "Sita":
        print("Hi, Alice")
    case "Bob":
        print("Hi, Bob")
    case _:  # We can use _ as a wildcard to match any value that doesn't match the other cases
        print("Hi, stranger")
