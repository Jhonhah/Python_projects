from random import randint, shuffle

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#available indices in the lists
letters_i = len(letters) - 1
numbers_i = len(numbers) - 1
symbols_i = len(symbols) - 1

#empty string to add other password elements
password = ''

#adding the components together
for n in range(nr_letters):
    password += letters[randint(0,letters_i)]

for n in range(nr_numbers):
    password += numbers[randint(0,numbers_i)]

for n in range(nr_symbols):
    password += symbols[randint(0,symbols_i)]

#shuffling it up
password_c = list(password)
shuffle(password_c)
final = ''.join(password_c)

print(final)


