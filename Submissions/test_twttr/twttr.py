def main():
    strs = input("Input: ")
    print(shorten(strs))

def shorten(word):
    vowels = ['a', 'e', 'i', 'o', 'u', "A", "E", "I", "O", "U"]
    for i in word:
        if i in vowels:
            word = word.replace(i, "")
    return f"{word}"


if __name__ == "__main__":
    main()
