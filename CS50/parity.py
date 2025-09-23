

x = int(input("What's x? "))

if x % 2 == 0: # the == ask if 0 is the remaider of the function 
    print("Even") # the == is the comparison operator  
else:
    print("Odd")


def main():
    y = int(input("WHat is y? "))
    if is_even(y):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    if n % 2 == 0:  # this line can be also written as  " return True if n % 2 == 0 else False" or "return n % 2 ==0" both of this can be done on a single line 
        return True
    else:
        return False


main()









