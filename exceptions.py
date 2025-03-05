"""_summary_
    Learning to use exceptions
"""


def main():
    try:
        number = int(input("Please enter an integer: "))
        answer = number/2

    except ValueError:
        print("Please check your input, that was not valid.")
    except Exception as e:
        print(f"You had an {e} error.")
    else:
        print(answer)
    finally:
        print("Goodbye!")


main()
