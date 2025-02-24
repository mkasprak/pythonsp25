"""
calculate area of triangle
"""


def main():
    base = float(
        input("Please enter the base of the triangle (inches assumed):  "))
    height = float(
        input("Please enter the height of the triangle (inches assumed):  "))
    area(base, height)


def area(base, height):
    triangle_area = base * height
    print(f"The area of the triangle is {triangle_area} sq inches.")


main()
