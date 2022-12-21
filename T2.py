import random

while True:
    dice=random.randint(1,6)
    dice2=random.randint(1,6)
    a=input("please enter s to start:")
    if a=="s":
        print(dice)
        if dice==6:
            print("your prize:",dice2)
            dice3=dice+dice2
            print("your score is",dice3)
        else:
            print("your score is",dice)
    else:
        break