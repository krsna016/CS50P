import random


def main():
    level = get_level()
    score = 0
    count = 0
    fix = 1
    while count < 10:
        generate_integer(level)
        while True:
            print(f"{x} + {y} = ", end="")
            try:
                sol = int(input())
            except ValueError:
                pass
            else:
                if x + y != sol and fix != 3:
                    print("EEE")
                    fix += 1
                elif fix == 3:
                    print(f"{x} + {y} = {x + y}")
                    break
                else:
                    score += 1
                    break
        fix = 1
        count += 1
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            pass
        else:
            if level == 1 or level == 2 or level == 3:
                break
    return level


def generate_integer(level):
    global x, y
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    elif level == 3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
    else:
        raise ValueError


if __name__ == "__main__":
    main()
