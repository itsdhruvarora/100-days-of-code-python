import random

names_string = input("Enter names separated by a comma: ")
names = names_string.split(",") 

n = len(names)

random_choice = random.randint(0, n-1)

print(names[random_choice] + " is going to pay the bill")