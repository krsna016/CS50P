def main():
    x = input()
    converted = convert(x)
    print(converted)

def convert(str_value):
    if ":)" in str_value:
        str_value = str_value.replace(":)","🙂")
    if ":(" in str_value:
        str_value = str_value.replace(":(","🙁")
    return str_value

main()
