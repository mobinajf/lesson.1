a=int(input("please enter first num:"))
b=int(input("please enter second num:"))
c=int(input("please enter third num:"))
if a<b+c and b<a+c and c<a+b:
    print("You can have a triangle with these sides")
else:
    print("errore")