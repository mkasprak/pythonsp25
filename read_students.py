"""

testing read methods
"""

def main():
    try:
        with open('example.txt', 'r') as file:
            content = file.read()
            print(content)
    except IOError:
        print("An IOError has occurred.")

main()    