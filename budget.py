'''
    Requirements:
    Design a Python program that prompts users to enter their total budget (ask them for their net monthly income) and amounts for spending categories:
    Housing (rent or mortgage)
    Utilities
    Groceries
    Transportation
    Health Care
    Personal Care
    Clothing
    Debt
    Calculate the percentage of the total budget spent in each category.
    Display the results in a user-friendly format using f-strings.
    Ensure your code is well-commented to explain the functionality of different sections.
'''

# Get input from user

budget = float(input("Please enter your net monthly income for the budget: "))
housing = float(input(
    "Please enter your housing costs (rent or mortgage plus HOA if you have it)"))


# Perform calculations
housing_percent = housing/budget * 100

# Output

print(f"Your housing is %{housing_percent:.1f} of your monthly budget.")
