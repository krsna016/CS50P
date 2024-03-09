# import random
# from random import choice
import random


def main():
    # # coin = random.choice(["Heads", "Tails"])
    # coin = choice(["Heads", "Tails"])
    # print(coin)

    # number = random.randint(1, 10)
    # print(number)

    cards = ["Jack","Queen","King"]
    random.shuffle(cards)
    for card in cards:
        print(card)



main()
