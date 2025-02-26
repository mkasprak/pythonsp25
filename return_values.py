"""
    Returning values from Functions

"""


def main():
    width, length = get_values()
    area = get_area(width, length)
    print(f"The area is: {area:,.2f}")


def get_values():
    width = float(input("Please enter the width in feet:  "))
    length = float(input("Please enter the length in feet:  "))
    return width, length


def get_area(w, l):
    area = w * l
    return area


main()
