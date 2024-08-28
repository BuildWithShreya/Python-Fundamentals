# Program to implement Tuple (create,access,update and delete Tuple).
# CREATE TUPLE
dept= ("COMP","IT","MECH","CIVIL","ELECTRICAL");
dist= ["PUNE","DHULE"];

# UPDATE TUPLE
college= ("GPP","GPA", dept, dist);
print(dept);
print(college);

# college[2]= "Nashik";   'tuple' object does not support item assignment
x= list(dept);
x[2]= dist;
y= tuple(x);

# ACCESS TUPLE
print(y);

# DELETE TUPLE
y= tuple();               #An assignment of empty tuple
print("Empty Tuple:",y);

# Create a tuple and find minimum and maximum number from it
tup1= (23,41,56,76,19)
m1= max(tup1)
print("Maximum value:",m1)
m2= min(tup1)
print("Minimum value:",m2)

# Program to find repeated items of tuple
t= (12,98,56,12,87,56)
print("Repeated items of a list:")
for i in range(0,len(t)):
    for j in range(i+1,len(t)):
        if(t[i]==t[j]):
            print(t[i],end=" ")
            
# Program to print number in words
print()
num = int(input("Enter any number:"))
t = list()
while num > 0:
    rem = num %10
    if rem == 0:
        t.append("Zero")
    elif rem == 1:
        t.append("One")
    elif rem == 2:
        t.append("Two")
    elif rem == 3:
        t.append("Three")
    elif rem == 4:
        t.append("Four")
    elif rem == 5:
        t.append("Five")
    elif rem == 6:
        t.append("Six")
    elif rem == 7: 
        t.append("Seven")
    elif rem == 8:
        t.append("Eight")
    elif rem == 9:
        t.append("Nine")
    num = num // 10  
for i in range(len(t)-1,-1,-1):
     print(t[i],end=" ")

print()    
a= (2,3,4,5,6)
b= (7,8,9)
print(len(a))
 
print(a*4)
print(a+b)

print(a[1:2])
print(a[:-3])

      
 
   
 
 
 

    



















