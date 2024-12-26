# TODO-1: Import and print the logo from art.py when the program starts.
from quopri import encodestring

import art
print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# TODO-2: What happens if the user enters a number/symbol/space?


def caesar():
    run = True
    while run:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        output_text = ""
        if direction == "decode":
            shift *= -1
        for letter in text:
            if letter in text:
                shifted_position = alphabet.index(letter) + shift
                shifted_position %= len(alphabet)
                output_text += alphabet[shifted_position]
            else:
                output_text += letter

        if direction == "encode":
            code = "encoded"
        else:
            code = "decoded"
        print(f"Here is the {code} result: {output_text}")

        choice = input("Do you wanna continue (yes/no):\n").lower()
        if choice == 'no':
            run = False


# TODO-3: Can you figure out a way to restart the cipher program?

caesar()



