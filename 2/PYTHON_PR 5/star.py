# Program to print star pattern
rows= int(input("Enter the no.of rows: "));
for i in range(0,rows):
    for j in range(0, rows-i-1):
        print(" ",end="");
    for k in range(0,2*i+1):
        print("*",end="");
    print();
for i in range(rows-1,0,-1):
    for j in range(rows, i, -1):
        print(" ",end="");
    for k in range(2*i-1,0,-1):
        print("*",end="");
    print();
    
print()
    
# Program to print star pattern using for loop
rows= 5;
for i in range(rows):
    for j in range(rows-i-1):      # rows-i-1
        print(" ",end="");
    for k in range(2*i+1):         # 2*i+1
        print("*",end="");
    print();
    
print()
# program to print star pattern using for loop
s="";
for i in range(5):
    s+= "*";
    print(s);
