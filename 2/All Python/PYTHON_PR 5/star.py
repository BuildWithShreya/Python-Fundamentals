# Program to print star pattern
num= int(input("Enter the no.of rows: "));
for i in range(0,num):
    for j in range(0, num-i-1):
        print(" ",end="");
    for k in range(0,2*i+1):
        print("*",end="");
    print();
for i in range(num-1,0,-1):
    for j in range(num, i, -1):
        print(" ",end="");
    for k in range(2*i-1,0,-1):
        print("*",end="");
    print();
    