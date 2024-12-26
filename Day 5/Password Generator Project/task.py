import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

my_pass = []

for i in range(nr_letters):
    a = random.choice(letters)
    my_pass.append(a)

for i in range(nr_symbols):
    a = random.choice(symbols)
    my_pass.append(a)

for i in range(nr_numbers):
    a = random.choice(numbers)
    my_pass.append(a)

print(my_pass)
password = ''.join(my_pass)
print(password)
random.shuffle(my_pass)
print(my_pass)
password = ''.join(my_pass)
print(password)
