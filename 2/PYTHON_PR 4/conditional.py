# program to implement conditional statements( if, if...else, elif, nested if)

# Even-Odd
num= int(input("Enter a number: "));
if(num%2==0):
    print(num,"is Even");
else:
    print(num,"is Odd");
    
# absolute value
num1= float(input("Enter a negative number: "));
res= abs(num1);
print("Absolute Value: ",res);
if(res>0):
    print(res,"is Correct Absolute Value");

# Largest Number among three numbers using elif statement
a= int(input("Enter first number:"));
b= int(input("Enter second number:"));
c= int(input("Enter third number:"));
if(a>b and a>c):
    print(a," is greater");
elif(b>a and b>c):
    print(b," is greater");
else:
    print(c," is greater");

# Largest Number among three numbers using nested if-else statement    
if(a>b):
    if(a>c):
        print(a," is greater");
    else:
        print(c," is greater");
else:
    print(b," is greater");
        
# Check year is leap or not
year= int(input("Enter year:"));
if(year> 999):
    if(year% 4==0):
        if(year% 100):
            if(year% 400):
                print(year,"is a leap year");
            else:
                print(year,"is not a leap year");
        else:
            print(year,"is not a leap year");
    else:
       print(year,"is not a leap year");
else:
    print("Please enter a valid year");

# Check number is positive, negative or zero
number= int(input("Enter a number:"));
if(number>0):
    print(number,"is positive");
elif(number<0):
    print(number,"is negative");
else:
    print(number,"is zero");

# Take marks of 5 subjects and display the grade
a,b,c,d,e= [int(x) for x in input("Enter marks of 5 subjects:").split()];
total= float(a+b+c+d+e);
per= (total/500)*100;
print("Percentage= ",per);
if(per>90):
    grade= "Distinction";
elif(per>80):
    grade= "A";
elif(per>70):
    grade= "B";
elif(per>60):
    grade= "C";
elif(per>40):
    grade= "Pass";
else:
    grade= "Fail";
print("Grade: ",grade);

    














       
        
        
        
        
        
    