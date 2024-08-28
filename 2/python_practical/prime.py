# prime
Flag= False
num= int(input("Enter number:"))
if(num==1):
    print(num,"is not prime number")
else:
    for i in range(2,num):
        if(num%i==0):
            Flag= True
    if(Flag):
        print(num,"is not prime number")
    else:
        print(num,"is prime number")
    
