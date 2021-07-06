n=int(input("enter the harshad number:"))
sum=0
a=n
while a!=0:
    r=a%10
    sum=sum+r
    a=int(a/10)
if n%sum==0:
    print("it is harshad number")
else:
    print("not")
