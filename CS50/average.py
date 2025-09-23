
import statistics

"""
statistics.mean(i1,i2) this function returns the average of the inputs
"""

def main():
    a = get_average()
    print(f"Average is {a}")

def get_average():
    i = int(input("What is i? "))
    j = int(input("What is J? "))
    avg = statistics.mean([i,j])
    return avg

main()

