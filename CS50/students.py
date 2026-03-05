"""
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")

"""

"""
students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append(f"{name} is in {house}")

for student in sorted(students):
    print(student)
this sorts the names in aplhabetical order
"""
import csv
"""
students = []

with open("students.csv") as file:
    reader = csv.reader(file) # read csv documentation omo read am 
    for name, house in reader:
        students.append({"name": name, "house": house })
    #for line in file:
        #name, house = line.rstrip().split(",")
        #student = {"name": name, "house": house}
        #students.append(student)
        # this wil run if a fuction is is called into place

"""

"""
def get_name(student): # can also be get_house
    return student["name"]
on the line 34 the key becomes key=get_name
"""

"""

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']}")
"""

name = input("what is your name?")
home = input("what is your nmae?")

