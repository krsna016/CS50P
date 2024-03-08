def main():
    string = input("Enter in camelCase : ")
    snake_case(string)

def snake_case(strs):
    for char in strs:
        if char.isupper():
            strs = strs.replace(char,"_"+char.lower())
    print(strs)

main()


