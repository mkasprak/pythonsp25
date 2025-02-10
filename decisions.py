'''
    clothing choice based on temperature
    Assuming going to school as the activity
'''

temp = float(input("What temperature is it in Fahrenheit:"))

if temp <= 0:
    print("Hmmm. I should at least bring a coat with me.")

elif temp < 32:
    print('Brr. Time for long sleeves')

elif temp < 50:
    print("Midwest Spring")

elif temp < 70:
    print("Pull out the grill!!!!")
    print("I'm going biking.")

elif temp < 120:
    print("Summer is here! Hit the beach.")

else:
    print("All of the air vents are covered by animals!")
