import random
import sys


def main():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            pass
        else:
            if level > 0:
                break

    random_nums = random.randint(1, level)

    while True:
        try:
            guess = int(input("Guess: "))
        except ValueError:
            pass
        else:
            if guess < 0:
                continue
            else:
                if guess < random_nums:
                    print("Too small!")
                elif guess > random_nums:
                    print("Too Large!")
                else:
                    print("Just right!")
                    sys.exit()


if __name__ == "__main__":
    main()
