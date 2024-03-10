import csv

name = input("What's your name : ")
home = input("Where's your home : ")
with open("csv_again.csv", "a") as file:
    # writer = csv.writer(file)
    writer = csv.DictWriter(file, fieldnames=['name', 'home'])
    # writer.writerow([name,home])
    writer.writerow({"home": home, "name": name})
