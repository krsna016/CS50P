import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if match := re.search(r'<iframe src="https?://(?:www.)?youtube\.com/embed/([a-zA-z0-9]+)"></iframe>', s):
        return f"https://youtu.be/{match.group(1)}"
    else:
        return None


if __name__ == "__main__":
    main()
