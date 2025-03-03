"""
    Tuples are lists that don't change

"""


def main():
    days_of_week = ("Sunday", "Monday", "Tuesday", "Wednesday",
                    "Thursday", "Friday", "Saturday")
    for day in days_of_week:
        print(day)
    print(len(days_of_week))


main()
