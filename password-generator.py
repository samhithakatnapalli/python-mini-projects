import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#for password in range(nr_letters):
    #print(random.choice(letters) + random.choice(numbers) + random.choice(symbols))
user_choice = ""
for letter in range(nr_letters):
    user_choice += random.choice(letters)
#print(user_choice)

for num in range(nr_numbers):
    user_choice += random.choice(numbers)
#print(user_choice)

for symb in range(nr_symbols):
    user_choice += random.choice(symbols)
print(user_choice)
converting = list(user_choice)
random.shuffle(converting)
final = ''.join(converting)
print(final)
