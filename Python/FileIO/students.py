# with open("names.csv") as file:
#     for line in file:
#         # row = line.rstrip().split(",")
#         # print(f"{row[0]} is in {row[1]}")
#
#         name, address = line.rstrip().split(",")
#         # print(f"{name} is in {address}")
#         print(f"{name:^10}: is in {address}")
#


# students = []
# with open("names.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         students.append(f"{name} is in {house}")
#
# for s in sorted(students, reverse=True):
#     print(s)


# students = {}
# with open("names.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         students[name] = house
#
# for i,j in students.items():
#     print(f"{i:^10} -> {j}")


# students = []
# with open("names.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         student = {}
#         # student["Name"] = name
#         # student["House"] = house
#         student = {"Name": name, "House": house}
#         students.append(student)
#
#
# def get_name(student):
#     return student["Name"]
#
# def get_house(student):
#     return student["House"]
#
#
# # for student in sorted(students, key=get_name): # Sort by name in dict inside list
# for student in sorted(students, key=get_house): # Sort by house in dict inside list
#     print(f"{student['Name']:^10} -> {student['House']}")
