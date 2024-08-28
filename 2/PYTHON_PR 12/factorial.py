# program to find factorial of number

def factorial(num):
    num= int(num)
    if(num<=1):
        return 1
    else:
        return num*factorial(num-1)
    
num= input("Enter a number:")
print("Factorial is",factorial(num))