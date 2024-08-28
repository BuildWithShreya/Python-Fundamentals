# program to check number is prime or not
num= 3457
Flag= False
if num== 1:
    print(num,"is not prime number")
elif num>1:
    for i in range(2, num):
        if(num%i)==0:
            Flag= True
            break
if Flag:
    print(num,"is not prime number")
else:
    print(num,"is prime number")
    