# import sys
# try:
#     print("Hello, My name is", sys.argv[1])
# except IndexError:
#     # print("Too Few Arguments!!")
#     pass


# import sys
# if len(sys.argv) <= 1:
#     print("Too Few Arguments!!")
# elif len(sys.argv) > 2:
#     print("Too Many Arguments!!")
# else:
#     print("My name is,", sys.argv[1])


# import sys
# if len(sys.argv) <= 1:
#     sys.exit("Too Few Arguments!!")
# elif len(sys.argv) > 2:
#     sys.exit("Too Many Arguments!!")
# print("My name is,", sys.argv[1])


import sys
if len(sys.argv) <= 1:
    sys.exit("Too Few Arguments!!")
print("My name is,", list(i for i in sys.argv[1:]))
