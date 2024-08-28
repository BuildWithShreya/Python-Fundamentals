# Program to implement set (create,access,update and delete set).
# CREATE SET
college= {"GPP","GPA","GPAN","GPN"};
print(college);

# UPDATE SET
college.add("GPD");
print(college);
y= list(college);
y[2]= "COEP";

# ACCESS SET
z= set(y);
print(z);

# DELETE SET
z.clear();
print(z);
college.clear();
print(college);

# PROGRAM TO FIND MAXIMUM AND MINIMUM VALUE IN A SET.
num= {12,32,54,76,10,98}
m1= max(num)
m2= min(num)
print("Maximum Value:",m1)
print("Minimum Value:",m2)

# Program to find the length of the set
number= {23,43,12,87,67,56,43}
length= len(number)
print("Length of the set:",length)

# Program to create a set, add member(s) in a set and remove one item from the set
num={12,24,36,56};
num.add(38);
print(num);
num.remove(24);
print(num);
num.discard(56);
print(num);
num.pop();
print(num);

# Progrm to perform following operations on a set: 
# intersection of set, union of set, set difference, symmetric difference, clear a set.
enrollB={23,25,27,29,31,33,35,37,39,41};
enrollC={51,25,55,57,59,37,63,65,67,69};
print("Intesection of Sets ");
print(enrollB.intersection(enrollC));
print("Union of sets ")
print(enrollB.union(enrollC));
print("Difference of sets ")
print(enrollB.difference(enrollC));
print("Symmetric Difference of sets ")
print(enrollB.symmetric_difference(enrollC));
enrollB.clear();
print(enrollB);



