# program to make simple calculator
def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def div(x,y):
    return x/y
print("select operation: ")
print("1. add: ")
print("2. subtract: ")
print("3. multiply: ")
print("4. division: ")
while True:
    choice= input("Enter choice(1/2/3/4): ")
    if choice in('1','2','3','4'):
        try:
            num1= float(input("Enter first number: "))
            num2= float(input("Enter second number: "))
        except ValueError:
            print("Invalid input")
            continue
        if choice== '1':
            print(num1,"+", num2,"=",add(num1,num2))
        elif choice== '2':
            print(num1,"-", num2,"=",subtract(num1,num2))
        elif choice== '3':
            print(num1,"*", num2,"=",multiply(num1,num2))
        elif choice== '2':
            print(num1,"/", num2,"=",div(num1,num2))
        next= input("let do next calculation yes/no:")
        if next== "no":
            break
    else:
        print("Invalid input")
        
        
    
