def main():
    hello("world")
    goodbye("world")

def hello(name):
    print("Hello, " + name + "!")

def goodbye(name):
    print("Goodbye, " + name + "!")


# We use __name__ == "__main__" to run the main function only if this file is being run directly
# If this file is being imported, the main function will not run
if __name__ == "__main__":
    main()
