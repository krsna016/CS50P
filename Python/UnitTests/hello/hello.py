def main():
    name = input("What's your name : ")
    output = hello(name)
    print(output)


# # Not returning any value
# def hello(name="Krsna"):
#     print(f"Hello, {name}")


# returning a value
def hello(name="Krsna"):
    return f"Hello, {name}"


if __name__ == "__main__":
    main()
