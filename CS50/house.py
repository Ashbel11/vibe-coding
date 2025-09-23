
soul = input("WHat class of soul do you have? ")

if soul == "Gambit": # if each one of them have the same return valve they can be reduced to a single if statemnet and combined using or with each valve and there comparism
    print("Lost")
elif soul =="Dealer":
    print("Danger")
elif soul == "Merciful":
    print("Lover")
elif soul == "Joyous":
    print("Happy")
else:
    print("What ARe You? ")

# this can be done in place of if and else statments

name = input("What is your name? ")

match name: # matchs a specfic output to a pattern/value 
    case "Ade": # if the output for several patterns/valves are simmilar they can be combined like this "case "Ade" | "Tunde" | "Samuel": "
        print("Jaja")
    case "Tunde":
        print("Enijoku")
    case "Samuel":
        print("Marere")
    case "Danny":
        print("Biobaku")
    case _: # the _ matchs with all or any value presnted which is not matched
        print("D Fuck? ")




 


