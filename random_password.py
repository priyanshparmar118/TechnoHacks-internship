import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '@', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to Password Generator :-")
n_letters = int(input("How many letters do you wand in your password?\n"))
n_symbols = int(input("How many synboles do you want in yout password?\n"))
n_numbers = int(input("How many numbers do you want in your password?\n"))
password = []

for i in range(1, n_letters+1):
    char = random.choice(letters)
    password += char

for i in range(1, n_symbols+1):
    char = random.choice(symbols)
    password += char

for i in range(1, n_numbers+1):
    char = random.choice(numbers)
    password += char
#print(password)    (to print random selected letters, symboles and numbers)

random.shuffle(password)
#print(password)    (to print shuffle random selected)

generated_password = ""
for i in password:
    generated_password += i

print("Random generated password is " ,generated_password)  # final random generated password