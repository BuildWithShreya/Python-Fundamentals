# Program to implement various loops

# For Loop
numbers= [2,3,4,5,6,7,8,9];
square= 0;
squares= [];
for value in numbers:
    square= value**2;
    squares.append(square);
print("List of Squares is",squares);
print()  
 
# While Loop
sum=0;
num= int(input("Enter a positive integer:"));
i= 1;
while(i<=num):
    sum= sum+i;
    i=i+1;
print("Sum of numbers till",num,"is=",sum);
print();

# nested loop
name= ["sara","siddhi","sai"];
sirname= ["Gore"];
for x in name:
    for y in sirname:
        print(x,y);
print();
        
# program to print star pattern using for loop
s="";
for i in range(5):
    s+= "*";
    print(s);
print();

# Program to find Factorial of the number.
num= int(input("Enter the number: "));
i= 1
fact= 1
while i<= num:
    fact*= i;
    i+= 1
print("Factorial of number is:",fact);
print();

# Program to print fibonacci series using for loop
a= 0;
b= 1;
fib= 0;
print("Fibonacci Series:");
for i in range(10):
    print(fib, end=" ");
    fib= a+b;
    a= b;
    b= fib;

# Program to print even number between 1 to 100 using while loop
n= 1;
print("Even numbers between 1 to 100: ");
while(n<=100):
    if(n%2==0):
        print(n,end=" ");
    n+= 1;
    
# Program to print sum of digits of given number
number= int(input("Enter the number:"));
sum= 0;
for digit in str(number):
    sum+= int(digit);
print("Sum of digits of",number,"is",sum);

# Program to reverse the given number
p= int(input("Enter the number:"));
m= p;
5reverse= 0;
while(m>0):
    rem= m% 10;
    reverse= (reverse*10)+rem;
    m= m// 10;
print("Reverse of",p,"is",reverse);

# Program to check number is palindrome or not
x= int(input("Enter the number:"));
y= x;
rev= 0;
while(y>0):
    rem1= y%10;
    rev= (rev*10)+rem1;
    y= y//10;
if(x==rev):
    print(x,"is palindrome");
else:
    print(x,"is not palindrome");
    
# Program to print star pattern using for loop
rows= 5;
for i in range(rows):
    for j in range(rows-i-1):
        print(" ",end="");
    for k in range(2*i+1):
        print("*",end="");
    print();
    

    




        
        
        
        
        
        

    
    
    
