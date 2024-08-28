# program to find factorial of number
num= int(input("Enter a number: "))
factorial= 1
if num<0:
    print("Factorial of ",num," is 0")
elif num==0:
    print("Factorial of ",num," is 1")
else:
    for i in range(1, num+1):
        factorial= factorial*i
    print("factorial of ",num," is ",factorial)