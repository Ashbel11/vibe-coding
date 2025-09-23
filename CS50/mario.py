
# ask ai on this code
def main():
    print_column(4)

def print_column(i):
    
    for _ in range(i):
        print("#")

main()

"""
the top code allows you tob eable to make a vertical column of 4 element 
but by adding this i = int(input("What is I? "))  you can now select how many element you need in your column

"""

def box():
    print_square(4)

def print_square(size):
    for k in range(size):
        for l in range(size): # this loop can be replaced using "print("#" * size)"
            print("#", end="")
        print() # this makes sure there is no new line 

box()


