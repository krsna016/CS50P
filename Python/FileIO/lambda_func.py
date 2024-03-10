students = []
with open("names.csv") as file:
    for line in file:
        student = {}
        name, house = line.rstrip().split(",")
        student = {"Name": name, "House": house}
        students.append(student)
for student in sorted(students, key=lambda student: student["Name"]):  # Lambda Function - Anonymous Func becouse func have no name
    print(f"{student["Name"]} --> {student["House"]}")
