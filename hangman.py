"""

    Hangman Start 
    you will finish by adding a list and checking against given letters
"""
import random

WORD_LIST = ("PYTHON", "COBOL", "JAVASCRIPT", "BASIC")


def game(answer, display):
    wrong = 0
    right = 0

    print("Welcome to Code of Fortune")
    print("You will guess letters until you have the word")
    print("If you have 5 wrong guesses you will lose!")
    while True:
        for item in display:
            print(item, end=" ")

        print("\n\n")
        bad_guess = True
        guess = input("Please enter a letter: ")
        guess = guess.upper()
        for letter in range(len(answer)):
            if guess == answer[letter]:
                display[letter] = guess
                right += 1
                bad_guess = False
                if right >= len(answer):
                    print("You Win!")
                    break
        if bad_guess == True:

            print("Wrong!")
            wrong += 1
            if wrong > 5:
                print("You Lose!")
                break


def main():
    answer = random.choice(WORD_LIST)
    display = []
    for i in range(len(answer)):
        display.append("_")

    game(answer, display)


main()
