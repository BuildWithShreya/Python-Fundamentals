import numpy as np
arr= np.array([1,2,3,4])
print(type(arr))

add= lambda x,y:x+y
print(add(20,20))

def myfunc(n):
    return lambda a:a*n
my= myfunc(2)
print(my(11))

class A:
    pass

print(10,20,30,sep="/")

print("{0} is a diploma portal",format("cwipedia"))

'''try:
    a= 20/0
    
except [ZeroDivisionError,TypeError]:
    print("Exception")

else:
    print("End")'''

def a():
    try:
        return 1
    finally:
        return 2
k= a()
print(k)

def b():
    try:
        print(1)
    finally:
        print(2)
m= b()
print()
    
print('1'==1)
print("{0} is a diploma portal",format("cwipedia"))

f = None
for i in range (5):
    with open("data.txt", "w") as f:
        if i > 2:
            break
print(f.closed)

import math
d= abs(math.sqrt(25))
print(d)
print(math.sqrt(25))

print('[%c]'%65)   # ascii to character A= 65

print('%x, %X' % (15, 15))   # f,F    small and capital x

f = None
for i in range (5):
 with open("data.txt", "w") as f:
     if i > 2: 
         break
print(f.closed)


print(min(max(False,-3,-4), 2,7))

class tester:
    def __init__(self,id):
        self.id= str(id)
        id= "224"
temp= tester(12)
print(temp.id)

print(math.floor(5.7))

x = "10"
result = int(x)
print(result)
 
x = "10"
print(x)

x = 3.7
result = round(x)
print(result)

x = "Hello"
print(type(x))

print(all([2,4,0,6]))      # false

print(any([2>8,4>2,1>2]))   # true

print(math.ceil(3.4))    # greatest integer

print("{0} is a diploma portal",format("cwipedia")) 

'''try:
    if '1'!= 1:
        raise "someError"
    else:
        print("someError has not occured")
except "someError":
    print("someError has not occured")'''
        
print('1'==1)     
        
'''class InvalidAgeException(Exception):
    pass
age= int(input("Enter a age: "))
if(age>=18):
    print("You are eligible for voting")
else:
    raise InvalidAgeException '''
    
print(abs(-5))
print(abs(5))
print(math.sqrt(25))

print(math.ceil(5.1))
    
def display(name,age):
 print("Student Name:",name)
 print("Student Age :",age)
display(name="Mohan",age=35)

def display(*m):
 print("Value of m=",m);
display(100,200,300,400,500,600,700,800,900)

'''def Addition():
 a=int(input("Enter First Number:"));
 b=int(input("Enter Second Number:"));
 c=a+b;
 return a,b,c;
m,n,p=Addition();
print("Addition of ",m," and ",n," is ",p);'''

a=100; #Global variable
def display():
 b=200; #local variable
 print("Local Variable b = ",b);
 print("Global Variable a= ",a);
display();
    
print(math.trunc(1.1));

import cmath
m=2+2j;
print("Result of exp(2+2j) =",cmath.exp(m));
x=cmath.log(m,2);
print("Result of log(2+2j,2) =",x);
x=cmath.sqrt(m);
print("Result of sqrt(2+2j) =",x);

import numpy as np
from scipy import linalg
a=np.array([[1.,2.],[3.,4.]]);
print(linalg.inv(a)) #find inverse of array

import pandas as pd;
dict={"Name":["Vishal","Mohan","Soham","Nilam"],"Salary":[12000,
13000,67000,11000]};
df=pd.DataFrame(dict);
print(df);

class Gmail:
 def send_email(self,msg):
     print("Sending {} from gmail".format(msg));
class Yahoo:
    def send_email(self,msg):
        print("Sending {} from Yahoo".format(msg));
class Email:
    provider=Gmail();
    def set_provider(self,p):
        self.provider=p;
    def send_email(self,msg):
        self.provider.send_email(msg);
        
client1=Email();
client1.send_email("Hello");
client1.set_provider(Yahoo());
client1.send_email("Hello")


    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
        
