"""
Playing with Functions!
Based on Mary had a little lamb
"""


def main():  # every program has a main function to coordinate the logic
    person = input("Enter a name: ")
    animal = input("Enter an animal: ")
    color = input("Enter a color: ")
    place = input("Enter a place: ")
    noun = input("Enter a noun: ")
    group_of_people = input("Enter a group of people: ")

    # call the mad libs function
    mad_libs(person, animal, color, place, noun, group_of_people)


def mad_libs(person, animal, color, place, noun, group_of_people):
    print(f"\n\n{person} had a little {animal},")
    print(f"Whose fleece was {color} as snow.")
    print(f"and any where that {person} went")
    print(f"The {animal} was sure to go.\n")
    print(f"It followed them to {place} one day")
    print(f"Which was against the {noun}.")
    print(f"It made the {group_of_people} laugh and play")
    print(f"to see a {animal} at {place}")


main()  # you have to call main for it to run
