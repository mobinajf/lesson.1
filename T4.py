print("please enter number or enter <exit>")
sum=0
n=0
while True:
    a=int(input("number or <0>for exit:"))
   
    if a==0:
        print("the sum of numbers:",sum)
        break
    n=float(a)
    sum=sum+n