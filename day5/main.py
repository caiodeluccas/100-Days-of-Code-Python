import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
number_letters = int(input("How many letters would you like in your password?\n"))
number_symbols = int(input(f"How many symbols would you like?\n"))
number_numbers = int(input(f"How many numbers would you like?\n"))

#Easy level:
easy_password = ""

for char in range(1, number_letters+1):
    easy_password += random.choice(letters)

for char in range(1, number_symbols+1):
    easy_password += random.choice(symbols)

for char in range(1, number_numbers+1):
    easy_password += random.choice(numbers)

print(f"The easy password is: {easy_password}\n")

#Hard Level:
password_list = []
hard_password = ""

for char in range(1, number_letters+1):
    password_list.append(random.choice(letters))

for char in range(1, number_symbols+1):
    password_list.append(random.choice(symbols))

for char in range(1, number_numbers+1):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)

for char in password_list:
    hard_password += char

print(f"The hard password is: {hard_password}")