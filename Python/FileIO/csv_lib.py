import csv

students = []
with open("names_houses.csv") as file:
    reader = csv.reader(file)
    # for row in reader:
    #     students.append({"Name" : row[0], "House" : row[1]})
    for name, home in reader:
        students.append({"Name": name, "House": home})

for student in sorted(students, key=lambda student: student["Name"]):  # Lambda Function - Anonymous Func
    print(f"{student["Name"]} --> {student["House"]}")
