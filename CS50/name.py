
import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
"""
elif len(sys.argv) > 2:
    sys.exit("Too mant arguments")
else:
    print("hello my name is ", sys.argv[1])
"""
for arg in sys.argv[1:]: # for the total number of inputed arguments
    print("hello, my name is ",  arg )
