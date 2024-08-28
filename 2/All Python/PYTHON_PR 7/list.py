# Program to implement List (create,access,update and delete list).

# CREATE LIST
poly= ["GPP","GPAN","GPA","GPN"];         
engi= ["COEP","VIT","PICT","PCCOE"];
dept= ["COMP","IT","CIVIL","MECH"];
college= [poly,engi];

# ACCESS LIST
print("Access list")
print(college);
print(poly[2]);
print(college[1]);

# UPDATE LIST
print("Update list")
college[1]= dept;
print(college);

# DELETE LIST
print("Delete list")
dept.remove("MECH");
print(dept);
college.clear();
print(college);

# Program to find sum of items in the list.
num= [23,45,67,89,12,90,54];
sum=0
for value in num:
    sum+=value
print("The sum of All Items in List Is: ",sum)

# Program to multiplies all items in the list.
mul=1
for value in num:
    mul=mul*value

print("The Multiplication of All Items in List Is: ",mul)

# Program to get largest  items in the list.
large=max(num)
print("The Largest item in the List is: ",large)
    
# Program to get smallest  items in the list.
small=min(num)
print("The Smallest item in the List is: ",small)

# Program to reverse the list.
num.reverse()
print("The Reverse item in the List is: ",num)

# Program to find common items from two lists
a= [23,45,56,78,12,43];
b= [49,23,45,98,12,65];
print("Common items from two lists are:")
result= [i for i in a if i in b];           # common items
print(result);

# Program to select even items of a list
m= [23,45,78,12,98,76]
print("Even items of list are:")
for i in m:
    if (i%2==0):
        print(i)
        














