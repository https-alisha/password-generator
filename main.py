#password generator

import random
import string

def generate_password(min_length, number=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if  number:
        characters += digits
    if special_characters:
        characters += special

    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meets_criteria = True

    return pwd

min_length = int(input("Enter the minimum length of the password: "))
pwd = generate_password(min_length)
print("the generated password is:", pwd)

generate_password(10)
