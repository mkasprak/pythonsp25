"""
    Importing and using the random module

"""

import random


def main():
    # demonstrating random
    print(random.randint(0, 10))

    # demonstrating abs()
    number = float(input("Please enter a negative number: "))
    absolute = abs(number)
    print(f"The absolute value of {number} is {absolute}")


main()
