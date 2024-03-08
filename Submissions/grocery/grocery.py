def main():
    store = {}
    while True:
        try:
            item = input().upper()
        except EOFError:
            print()
            break
        else:
            if item not in store:
                store[item] = 1
            else:
                store[item] += 1

    sorted_store = dict(sorted(store.items()))
    show_items(sorted_store)

def show_items(s):
    for i in s:
        print(f"{s[i]} {i}")

if __name__ == "__main__":
    main()
