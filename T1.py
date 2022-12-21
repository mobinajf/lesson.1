import random

pc_number=random.randint(0,20)
guess=0
while True: 
    user_number=int(input("enter number:"))
    if pc_number==user_number:
        print("you win")
        guess=guess+1
        print("your guess number:",guess)
        break
    if pc_number>user_number:
        print("boro balatar")
        guess=guess+1
    elif pc_number<user_number:
        print("boro paentar")
        guess=guess+1