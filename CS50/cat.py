"""

i = 3
while i != 0:
    print("meow")
if you runthis the output wil be a continous and not stop at 3 but will repeat itself since both statments are true   
if in an ifinte loop crtl c will stop the loop inthe terminal
"""

i = 3
while i!= 0:
    print("meow")
    i = i - 1 # when this done as it repaets itself the inital value will con tinue ot reduce untils is 0


n = 1
while n <= 3: # using this you will get 3 moews' you can also dothis in another formatby changing the <= to < and starting the intger at 0
    print("yeah")
    n = n + 1 # this can be rewritten as n += 1

for k in [0, 1, 2]: # this can be simplifed by using a function called range
    print("meow")

for _ in range(2): # the _ can be used as a variable if you don't have a variable name for your value
    print("damn")

print("no my boy \n" * 2, end="") # the end="" is an function of the print

while True:
    p = int(input("What is p? "))
    if p > 0:
        break
for _ in range(p):
    print("meow")

def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        j = int(input("What is number? "))
        if j > 0:
            return j

def meow(j):
    for _ in range(j):
        print("meow")
        


