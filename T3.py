import random

n=int(input("please enter n:"))
num=[]
while True:
    b=random.randint(0,n)
    if b not in num:
        num.append(b)
    elif len(num)==n:
        print(num)
        break