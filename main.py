import random 
letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z', 
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '+', '_', '-', '`', '~', '|', '.', ',']

print('Welcome to the PyPassword Generator!!')
num_letters = int(input("How many letters would you like in your Password?\n"))
num_symbols = int(input(f"How many symbols would you like in the Password?\n"))
num_numbers = int(input(f"How many numbers would you like in the Password?\n"))

password_list = []
for char in range(1, num_letters + 1):
        password_list.append(random.choice(letter))
for char in range(1, num_symbols + 1):
        password_list.append(random.choice(symbols))
for char in range(1, num_numbers + 1):
        password_list.append(random.choice(numbers))
        random.shuffle(password_list)            
password = ''
for char in password_list:
    password += char 
print(f"Your password that is generated is " + password)