def double_penny(days, amount=0.01):
    """
    Recursive function to calculate the amount of money when a penny is doubled every day.

    days: int - The number of days over which the penny is doubled.
    amount: float - The current amount of money. Default is 0.01, representing 1 penny.
    return: float - The total amount of money after the specified number of days.
    """
    if days == 1:
        return amount
    else:
        return double_penny(days - 1, amount * 2)

# Example usage


def get_input():
    print("I am giving you a penny today, two tomorrow, and I will keep doubling")
    print("For as many days as you want. ")
    days = int(input("Enter the number of days: "))
    return days


def main():
    days = get_input()
    total_amount = double_penny(days)
    print(f"Total amount after {days} days: ${total_amount:,.2f}")


main()
