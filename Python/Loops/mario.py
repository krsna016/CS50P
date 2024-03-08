# print("#\n"*10,end="")


# def main():
#     col = int(input("Enter number of columns : "))
#     print_column(col)
# def print_column(num):
#     for _ in range(num):
#         print("#")
# main()


# def main():
#     rows = int(input("Enter number of rows : "))
#     print_rows(rows)
# def print_rows(num):
#     # for _ in range(num):
#     #     print("#",end = "")
#     # print()
#     print("#"*num)
# main()


# def main():
#     num = int(input("Enter a num : "))
#     print_square(num)
# def print_square(num):
#     print(f"The square of {num} is : {num**2}")
# main()


def main():
    size = int(input("Enter a num : "))
    print_square(size)
def print_square(size):
    for _ in range(size):
        print("#  "*size)
main()