# even-odd
num= int(input("Enter number: "))
if(num%2==0):
    print(num,"is even")
else:
    print(num,"is odd")
    
# abs value
num1= int(input("Enter negative number: "))
res= abs(num1)
print(res)
if(res>0):
    print(res,"is correct absolute value")

# largest
a= int(input("Enter number:"))
b= int(input("Enter number:"))
c= int(input("Enter number:"))
if(a>b and a>c):
    print(a,"is greater")
elif(b>a and b>c):
    print(b,"is greater")
else:
    print(c,"is greater")
    
# leap year
year= int(input("Enter year:"))
if(year%4==0):
    print(year,"is leap year")
elif(year<999):
    print("Enter correct year")
else:
    print(year,"is not a leap year")
    
# positive, negative, zero
a1= int(input("Enter number:"))
if(a1>0):
    print("positive")
elif(a1<0):
    print("negative")
else:
    print("zero")
    
# grade

m,n,p,x,y= [int(x) for x in input("Enter marks: ").split()]
total= m+n+p+x+y
per= (total/500)*100
print(total)
print(per)
if(per>90):
    grade= 'a'
elif(per>80):
    grade= 'b'
elif(per>60):
    grade= 'c'
elif(per>35):
    grade= 'pass'
else:
    grade= 'fail'
print("Grade= ",grade)

    
    
    