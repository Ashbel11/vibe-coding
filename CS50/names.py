"""
names = []

for _ in range(3):
    names.append(input("What is your name? "))

for name in sorted(names):
    print(f"hello, {name}")

"""
"""
name = input("What is your name?")
# file = open("names.txt", "w") where "w" writes the  values of each of them
# file = open("name.txt","a")
with open("names.txt","a") as file:
    file.write(f"{name}\n")
#file.close()
"""
with open("names.txt","r") as file:
    lines = file.readlines()

for line in lines:
    print("hello,",line.rstrip())
"""
with open("name.txt", "r") as file:
    for line in file:
        print("hello,",line.rstrip())
"""
"""
manes = []
with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(name):
    print(f"hello, {name}")


"""

