def main():
    possibles = [25,10,5]
    amount = 50
    change = 0
    while amount >= 0:
        prompt = int(input("Insert Coin: "))

        if prompt in possibles:
            amount -= prompt

        if amount <= 0:
            print("Change Owed:",abs(amount))
            return

        print("Amount Due:",amount)

main()
