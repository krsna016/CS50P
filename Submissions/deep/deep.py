def main():
    prompt = input("What is the answer to the Great Question of Life, the Universe and Everything ? : ")
    match prompt.lower().strip():
        case "42" | "forty-two" | "forty two":
            print("Yes")
        case _:
            print("No")

main()
