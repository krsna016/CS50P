import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    # if matches := re.search(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$", ip):
    regex = r"^((?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
    if matches := re.search(regex, ip):
        return True
    return False

if __name__ == "__main__":
    main()
