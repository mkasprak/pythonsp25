# Generator function that produces all possible two-letter combinations
# from a list of characters provided as input.

def two_letter_combinations(characters):
    """
    This generator function takes a list of characters and yields
    all possible two-character combinations formed by selecting
    one character for the first position and another (or the same)
    for the second position.

    Parameters:
    characters (list): A list of single-character strings.

    Yields:
    str: A two-character string representing a combination.
    """
    # Outer loop selects the first character in the pair
    for first in characters:
        # Inner loop selects the second character in the pair
        for second in characters:
            # Combine the two characters into a string and yield it
            yield first + second


def main():
    """
    Main function to test the generator.
    Creates a list of 5 characters, then iterates through all
    possible two-letter combinations and prints them one by one.
    """
    # Define a list of 5 original characters
    char_list = ['x', 'y', 'z', 'm', 'n']

    # Call the generator function and print each combination
    print("All possible two-letter combinations:")
    for combo in two_letter_combinations(char_list):
        print(combo)


# Run the main function to execute the program
main()
