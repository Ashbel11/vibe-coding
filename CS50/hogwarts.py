
students = ["Dami", "Gabi", "Trent"]

print(students[2]) # within a list the first item in a list is at location 0 or 0 indexed

for student in students: # ask about this line
    print(student) # student does not need to be initalized


for i in range(len(students)): # the len function returns the number of items in an object
    print(i + 1, students[i]) # omo ask ai about his function

"""
tads = ["Boye", "Dada", "Juju"]
homes =["Jaja", "Maya", "Abule"]
"""

yams = { 
    "Ted": "Enijoku",
    "Richard": "Jaja", 
    "Lanre": "Yct"} # this format is known as a dictionary

print(yams["Ted"]) # the info before the colon is used as key assigned to the value

for yam in yams: 
    # print(yam) this wil give an output of the keys
    print(yam , yams[yam], sep=",") # this give an output of both the key and it's value and the "sep=" "" is used as separator in the output 


kids = [
    {"Name": "Debo", "Hostel": "Femi G", "Course": "ZLY"},
    {"Name": "Ladi", "Hostel": "High R", "Course": "BNN"},
    {"Name": "Happy", "Hostel": "Complex", "Course": None} # this is a dictionary within a list doing this don't forget the comma  None is a function which implys it name
]

for kid in kids:
    print(kid["Name"], kid["Hostel"], kid["Course"], sep=", ")


