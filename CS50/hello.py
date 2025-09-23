# started with the function print("Hello world")
name = input("what is your name? ")
# can also add another function print containing the input value instead of using + or , 
# + meaning concatination
# this str.strip() help to remove white space from the string
name = name.strip()
# str.capitalize() help to capitalize the input
name = name.capitalize()

# two or more functions to string
name = name.strip().title()

# confamation of line 23
first, middle, last = name.split(" ") # when running the code this line will only run if there are 3 str inputed  

print("Hello, " + middle )
"""
this for preparing multi line comment
\n meanes a new line
when you have a \"str\" in the print function you it gives you "str" when it si run
f in front of the " this tell python that it should format the string  
"""
# Two str values can be split or selected by using a function as str.split and can be asigned to a value of two or more things like first , last 

def hello():
    print("hello")
oroko = input("What is your name ?")
hello()
print(oroko)


def helox(to="World"):
    print("hello", to )

helox
suxce = input("Who the fuck are you? ")
helox(suxce)


def main():
    nama = input("why the fuck? ")
    nama = nama.capitalize
    print(nama)

def hoho(mo="world baby"):
    print("Hello" , mo)

main()


