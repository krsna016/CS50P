def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    flag = True
    if not 2 <= len(s) <= 6:
        flag = False
    elif not s.isalnum():
        flag = False
    elif s[0].isdigit():
        flag = False
    elif not s[0].isdigit() and not s[-1].isdigit() and not s[1:-2].isalpha():
        flag = False

    # Checking that number not starts with zero(0)
    nums = ""
    for i in s:
        if i.isdigit():
            nums += i
    if nums:
        if nums == "0" or nums[0] == "0":
            flag = False
    # Checking that number not comes in middle
    k = len(s)
    while k != 2:
        if not s[k - 1].isdigit() and not s[1:k].isalpha():
            flag = False
            break
        k -= 1

    return flag


main()
