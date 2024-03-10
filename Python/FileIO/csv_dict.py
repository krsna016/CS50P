import csv

students = []
with open("including_header.csv") as file:
    reader = csv.DictReader(file)
    # for row in reader:
    #     students.append({"Name" : row[0], "House" : row[1]})
    for row in reader:
        students.append({"Name": row["Name"], "House": row["House"]})
#
# for student in sorted(students, key=lambda student: student["Name"]):  # Lambda Function - Anonymous Func
#     print(f"{student["Name"]} --> {student["House"]}")
print(students)