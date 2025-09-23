
# this is done to make sure the input is the correct data type
# ValueError
try:  
    x = int(input("What is x? "))
    print(f"x is {x}")
except ValueError:
    print("x is not an integer")


#NameError
# the NameError will occur if the else function is removed
try:
    y = int(input("What is y? "))
except ValueError:
    print("y is not an integer")
else:
    print(f"y is {y}")

# in terms of loop

while True:
    try:
        a = int(input("what is a "))
    except ValueError:
        print("a is not an integer")
    else:
        break
print(f"a is {a}")

# in terms of function

def main():
    b = get_integer()
    print(f"b is {b}")

def get_integer():
    while True:
        try:
            b = int(input("What is b? "))
        except ValueError:
            print("b is not an integer")
        else:
            return b
# lines 37 to 44 can be written as:
"""
def get_integer():
while True:
try:
return int(input("What is b "))
except ValueError:
pass

this is another way of writing the same function
def main():
    b = get_integer("What is b? ")
    print(f"b is {b}")

def get_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Input is not an integer")

main()
"""

main()
