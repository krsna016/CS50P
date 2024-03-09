import pprint
import requests
import sys


def main():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    except requests.RequestException:
        pass
    obj = response.json()
    # pprint.pprint(obj)

    if len(sys.argv) == 1:
        sys.exit("Missing command-line argument")
    elif sys.argv[1].isalpha():
        sys.exit("Command-line argument is not a number")
    elif len(sys.argv) == 2:
        amount = obj["bpi"]["USD"]["rate_float"] * float(sys.argv[1])
        print(f"${amount:,.4f}")


if __name__ == "__main__":
    main()
