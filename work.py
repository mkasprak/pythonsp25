"""
    Write a Python program that uses if-else statements and:

Asks the user for their age and converts the input to an integer.
Check to see if the user is old enough to drive.
Check to see if the user can vote.
Check to see if the user can legally buy alcohol.
Check to see if the user is eligible for a senior discount.
Prints all the results on the screen, ensuring the output is straightforward and user-friendly.
    """

# I hope you don't mind my silly comments. Originally I wanted to play around with

age = int(input("How old are you? (Please answer in whole numbers): "))

if age <= 0:
    print("Wow, so you just don't exist, huh? That or you're a time traveler. Congrats on breaking the time stream or whatever.")

if age < 16:
    print("You are not old enough to obtain a driver's license yet.")
    if age <= 1:
        print("Awww! Who's a cute widdle baby? Who needs theiw pacifiew? You do! You do!")

    elif age <= 2:
        print("Your little legs are trembling beneath your own weight. Can you even walk?")

    elif age <= 4:
        print("I think you're old enough to start learning taekwondo...")

    elif age == 5:
        print("The big 5! You're now old enough to start preschool!")

    elif age == 6:
        print("Welcome to kindergarten!")

    elif age <= 13:
        print("Oh, a middle schooler, huh? LMAO, good luck.")

    elif age <= 15:
        print("Oh no, you're in high school now. Brace yourself...")
else:
    print("You are old enough to obtain a driver's license.")

if age < 18:
    print("You are not old enough to vote yet.")

    if age <= 20:
        print(
            "Oof. Becoming a legal adult AND voting rights? You get the double whammy...")
        print("Make wise voting decisions from now on.")

    elif age <= 25:
        print("Oh, wow, you're old. I can't believe you can legally buy alcohol...")

else:
    print("You are old enough to vote.")


if age < 21:
    print("You are not old enough to legally buy or drink alcohol yet.")
else:
    print("You are old enough to legally buy alcohol. ")


if age < 65:
    print("You are not eligible for a senior discount.")
    if age <= 30:
        print("Now you're responsible for your own health insurance! Welcome to the real world :)")

    elif age <= 40:
        print("Oh, people are DEFINITELY teasing you for being old now. Have fun with that revelation. Definitely not a senior.")

    elif age <= 50:
        print("Now you're getting ACTUALLY middle-aged. Sorry, bud, no hard feelings. You're not a senior, though, so that's a plus!")

    elif age <= 60:
        print("Congrats on making it over the hill. Still not eligible for the senior discount, though...")

    elif age < 65:
        print("Oooh, so close! You're just barely shy of that senior discount!")

else:
    print("You are eligible for a senior discount.")

if age <= 84:
    print("Congratulations! You now qualify as a senior citizen. Get dat bank!")

elif age <= 100:
    print("I submit myself to you, wise elder. Teach me your ways.")

elif age <= 122:
    print("Whoa. You are a certified granny. Enjoy your retirement!")

else:
    print(
        f"Are... are you really {age}? Either you're some being beyond human comprehension, or that's just a straight up lie.")
    print("\n...and yes, you still qualify for that senior discount.")
