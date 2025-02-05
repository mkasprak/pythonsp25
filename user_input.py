"""_summary_
    Getting user input
"""

first_name = input("Please enter your first name: ")
print(f"Hello {first_name}")
# preferred way to convert to an int
age = int(input("How old are you? (Use numerals)  "))
# age = int(age)
new_age = age + 1
print(f"Next year you will be {new_age}. ")
print("You will be " + str(new_age) + " next year.")
print("_" * 50)
