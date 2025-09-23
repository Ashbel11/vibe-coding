score = int(input("What is your score? "))

if score >= 90 and score <= 100:
    print("Grade: A")
elif score >= 80 and score < 99:
    print("Grade: B")
elif score >= 70 and score < 80:
    print("Grade: C")
elif score >= 60 and score < 70:
    print("Grade: D")
else:
    print("Grade: F")

# this can be also written as:

WhatScore = int(input("What is your score? "))

if 90 <= WhatScore <= 100:
    print("Grade: A")
elif 80 <= WhatScore < 99:
    print("Grade: B")
elif 70 <= WhatScore < 80:
    print("Grade: C")
elif 60 <= WhatScore < 70:
    print("Grade: D")
else:
    print("Grade: F")

num = int(input("Score: "))

if num >= 90:
    print("Grade: A")
elif num >= 80:
    print("Grade: B")
elif num >= 70:
    print("Grade: C")
elif num >= 60:
    print("Grade: D")
else:
    print("Grade: F")



