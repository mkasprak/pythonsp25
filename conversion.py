'''
    Create a Python program that converts kilograms to pounds. 
    Use at least four different samples to convert. 
    A sample of the math is provided below; do not use the same 
    example in your program.

    Kilograms to Pounds Conversion:
    To convert kilograms (kg) to pounds (lb), use the formula:

    Pounds (lb) = Kilograms (kg) * 2.20462

    Example: 5 kg * 2.20462 = 11.0231 lb

'''
conversion_rate = 2.20462

kilo_1 = 150
kilo_2 = 200


pound_1 = kilo_1 * conversion_rate
pound_2 = kilo_2 * conversion_rate

print(f"{kilo_1} kilograms = {pound_1:.1f} pounds")
print(f"{kilo_2} kilograms = {pound_2:.1f} pounds")
