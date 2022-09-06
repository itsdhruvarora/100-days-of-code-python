import random
print("Welcome to the Pypass_list Generator!\n")
alpha = int(input("How many letters would you like in your pass_list: "))
num = int(input("How many numbers would you like in your pass_list: "))
sym = int(input("How many symbols would you like in your pass_list: "))

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


pass_list = []
for char in range(0, alpha):
    pass_list += random.choice(letters);

for char in range(0, num):
    pass_list += random.choice(numbers);

for char in range(0, sym):
    pass_list += random.choice(symbols);

random.shuffle(pass_list)
# print(pass_list)

password = ""
for x in pass_list:
    password += x;

print(password)
