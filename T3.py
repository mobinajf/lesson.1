for i in range(20):
 S1=float(int(input("average1:")))
 S2=float(int(input("average2:")))
 S3=float(int(input("average3:")))
 name=input("please enter your full name:")
 mean=(S1+S2+S3)/3
 if mean>=17:
    average="greate"
 if 17>mean>=12:
    average="normal"
 elif mean<12:
    average="fail"
 print(average)