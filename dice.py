import random

x = "y"

while x == "y":
    number = random.randint(1, 6)
    
    if number == 1:
        print("---------")
        print("|       |")
        print("|   O   |")
        print("|       |")
        print("---------")
        print("You got a 1")
    if number == 2:
        print("---------")
        print("| O     |")
        print("|       |")
        print("|     O |")
        print("---------")
        print("You got a 2")
    if number == 3:
        print("---------")
        print("| O     |")
        print("|   O   |")
        print("|     O |")
        print("---------")
        print("You got a 3")
    if number == 4:
        print("---------")
        print("| O   O |")
        print("|       |")
        print("| O   O |")
        print("---------")
        print("You got a 4")
    if number == 5:
        print("---------")
        print("| O   O |")
        print("|   O   |")
        print("| O   O |")
        print("---------")
        print("You got a 5")
    if number == 6:
        print("---------")
        print("| O   O |")
        print("| O   O |")
        print("| O   O |")
        print("---------")
        print("You got a 6")
    
    x = input("\n Press y to roll again or n to exit \n ")