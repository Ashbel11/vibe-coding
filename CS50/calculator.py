# the x and y variables can also have an int function to make them integers instead of making another variable
x = input("What is x ")
y = input("What is y ")

# for two or more intgers to operate they need to have the int function

z = int(x) + int(y)  
# if this is done without the function int it just joins both values together like a string



print(z)

# float function is used for decimals while int for whole numbrs
# it has a presice valve after the decimal
 
p = float(input("What is p? "))
q = float(input("What is q? "))

f = round(p + q) # this help to round the valves present
""" 
the round function can limited by using " , " with the significant figure needed
it can alsobe done by using the f string f"{:.nf}" where is the number of sf

"""

print(f"{f:,}") # the f"{:,}" is used to format the string (it is called an f string




def main():
    z = int(input("what us z? "))
    print("z squared is ", squared(z))

def squared(n):
    return n ** 2 # can be done using pow(, n) or with n*n


if __name__ == "__main__":
    main()

