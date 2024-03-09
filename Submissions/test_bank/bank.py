def main():
    greeting = input("Greet : ")
    value(greeting)

def value(greeting):
    greeting = greeting.lower().strip()
    amount = ""
    if greeting.startswith("hello"):
        amount = "0"
    elif greeting.startswith("h"):
        amount = "20"
    else:
        amount = "100"
    return int(amount)


if __name__ == "__main__":
    main()
