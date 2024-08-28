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
        
 # methods       
list1= [1,2,3,4,5];
print(type(list1));

list1.append(3);
print(list1);

list2= [6,7,8,9,0];
list1.extend(list2);
list1.extend([9,8,6])
print(list1);

del list1[3];
print(list1);

print(len(list1))

print(list1+list2);

gpp= ['comp', 'civil','mech','e&tc'];
print(gpp*4);

z= 'comp' in gpp             # membership
print(z)

for x in gpp:                # Iterative
    print(x)

alpha= ['a','b','c','d']
print(alpha[2])
print(alpha[-1])
print(alpha[1:4])
print(alpha[2:])
print(alpha[-1:])
print(alpha[:-1])
print(alpha[:2])
print(alpha[:-3])
print(alpha[:])
print()

a= [1,2,3,4,4,4,1]
b= [5,6,7,8]
c= max(a)
print(c)
d= min(a)
print(d)
print(a.count(4));
a.reverse()
print(a)

print(a.index(3))
b.insert(2,24);
print(b)

b.pop(3)
print(b)
print(b.pop())
print(b)

a.sort()
print(a)

print(a[:-1])
print(a[1:4])
print(a[-1:])

x,y= [1,2],[3,4]
print(x)
print(y)














