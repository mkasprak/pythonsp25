"""
    Dictionaries

"""

english_to_spanish = {
    "one": "uno",
    "two": "dos",
    "three": "tres",
    "four": "cuatro",
    "five": "cinco",
    "six": "seis",
    "seven": "siete",
    "eight": "ocho",
    "nine": "nueve",
    "ten": "diez"
}

# Accessing Python Dictionary Elements:
# Using Keys: To access a specific value, use the key enclosed in square brackets.

item = english_to_spanish['two']
print(item)


# get() Method: Safely access values using the get() method to avoid KeyError.

# Access 'USA' as default if 'country' doesn't exist
value = english_to_spanish.get('eleven', "11")
print(value)


# Iterating through Keys: Use a loop to access all keys and their corresponding values.

for key in english_to_spanish:
    print(key, english_to_spanish[key])  # Access both key and value


# Using Items: Iterate through key-value pairs using the items() method.

for key, value in english_to_spanish.items():
    print(key, value)  # Access both key and value
