#Program to swap two numbers if they are even using simple if
print("Program to swap two numbers if they are even using simple if")
x=int(input("Enter 1st Number : "))
y=int(input("Enter 2nd Number : "))
print("X= ",x,"  Y= ",y)
if((x%2==0) and (y%2==0)):
    temp=x
    x=y
    y=temp
    print("Swapped Numbers are X= ",x," and Y= ",y)

#Program to find division of two numbers for non zero denominator using if-else
print("\nProgram to find division of two numbers for non zero denominator using if-else")
x=int(input("Enter 1st Number : "))
y=int(input("Enter 2nd Number : "))
print("X= ",x,"  Y= ",y)
if(y!=0):
    z=x/y
    print('Results are : ',z)
else :
    print("results are infinity")

#Program to find biggest of 3 numbers using nested if
print("\nProgram to find biggest of 3 numbers using nested if")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if num1 >= num2:
    if num1 >= num3:
        largest = num1
    else:
        largest = num3
else:
    if num2 >= num3:
        largest = num2
    else:
        largest = num3

print("The largest number is", largest)

