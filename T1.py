import math

a=int(input("please enter first number:"))
op=input("please enter operation:")
if op=="+":
    b=int(input("please enter second number:"))
    result=a+b
if op=="-":
    b=int(input("please enter second number:"))
    result=a-b
if op=="*":
    b=int(input("please enter second number:"))
    result=a*b
if  op=="/":
    b=int(input("please enter second number:"))
    if b==0:
          result="erorre"
    elif b!=0:
          result=a/b
if op=="cos":
    num=math.radians(a)
    result=math.cos(num)
if op=="sin":
    num1=math.radians(a)
    result=math.sin(num1)
if op=="tan":
    num2=math.radians(a)
    result=math.tan(num2)
if op=="cot":
    if a==0:
        result="error"
    elif a!=0:
        num3=math.radians(a)
        result=1/math.tan(num3)
if op=="factorial":
    result=math.factorial(a)
if op=="radical":
   if a>=0:
      result=math.sqrt(a)
    
print(result)