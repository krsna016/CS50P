import pprint

list_dicts = []
names = ["Alice", "Bob", "Charlie", "David", "Eve"]
classes = ["I", "II", "III", "IV", "V"]
surname = ["Smith", "Johnson", "Williams", "Brown", None]
jobs = ["Engineer", None, "Lawyer", "Teacher", "Nurse"]

for i in range(5):
    dict = {}
    dict["Name"] = names[i]
    dict["Class"] = classes[i]
    dict["Surname"] = surname[i]
    dict["Job"] = jobs[i]
    list_dicts.append(dict)
pprint.pprint(list_dicts)
# print()
# for i in list_dicts:
#     print(i["Name"],i["Class"],i["Surname"],i["Job"],sep=" --> ")