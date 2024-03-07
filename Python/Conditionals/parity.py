def main():
    x = int(input("Enter a number: "))
    if parity_check(x):
        print(x, "is even")
    else:
        print(x, "is odd")


def parity_check(num):
    # # Returns boolean value
    # if num % 2 == 0:
    #     return True
    # else:
    #     return False

    # # Also:
    # return True if num % 2 == 0 else False

    # Also:
    return num % 2 == 0


main()
