
"""
Advanced try and except statements - catching specific 
"""


def main():
    try:
        number = int(input("Please enter an integer. "))
        print(f"10 / {number} = {10/number}")
    except ValueError:
        print("Sorry, that is not a valid entry. Please enter an integer")
    except ZeroDivisionError:
        print("Sorry, we can't divide by 0!")
    except Exception as e:
        print(e)


main()
