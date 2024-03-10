# name = input("What's your name ? : ")
# print(f"Hello, {name}")


# names = []
# for _ in range(3):
#     names.append(input("What's your name ? : "))
# for name in sorted(names):
#     print(f"Hello, {name}")


# # We need to close the file:
# name = input("What's your name : ")
# file = open("names.txt","a")
# file.write(name+" ")
# file.close()


# # Automatically take care of closing the file:
# name = input("What's your name : ")
# with open("names.txt","a") as f:
#     f.write(f"{name}\n")


# with open("names.txt", "r") as file:
#     lines = file.readlines()
# for line in lines:
#     # print(f"Hello, {line}", end="")
#     print(f"Hello, {line.rstrip()}")


# with open("names.txt", "r") as file:
#     for line in file:  # Same as "for line in file.readlines():"
#         print(f"Hello, {line.rstrip()}")


#
# names = []
# with open("names.txt", "r") as file:  # Same as "with open("names.txt") as file:"
#     for line in file:
#         names.append(line.rstrip())
# for name in sorted(names):
#     print(f"Hello, {name}")


# with open("names.txt", "r") as file: # Same as "with open("names.txt") as file:"
#     lines = file.readlines()
# for line in sorted(lines):
#     print(f"Hello, {line.rstrip()}")


# with open("names.txt", "r") as file:  # Same as "with open("names.txt") as file:"
#     for line in sorted(file):
#         print(f"Hello, {line.rstrip()}")
#


# This is how we sort in reverse:
with open("names.txt", "r") as file:  # Same as "with open("names.txt") as file:"
    for line in sorted(file, reverse=True):
        print(f"Hello, {line.rstrip()}")
