def main():
    str = input("Input: ")
    vowels = ['a','e','i','o','u',"A","E","I","O","U"]
    for i in str:
        if i in vowels:
            str = str.replace(i,"")
    print("Output:",str)
main()
