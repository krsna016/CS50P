def main():
    n = get_int("Enter : ")
    print(f"n is {n}")
    pass


def get_int(prompt):
    while True:
        try:
            # Here return will break the loop and return the value
            return int(input(prompt))
        except ValueError:
            # print("Please enter a Integer Value!!")
            # We can use "pass" if we don't want to do/prompt anything
            pass


main()
