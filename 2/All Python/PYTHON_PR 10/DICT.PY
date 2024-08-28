# Program to implement Dictionary (create,access,update and delete Dictionary).
# CREATE DICTIONARY
city= {1:"Pune",2:"Nagar",3:"Dhule",4:"Mumbai"};
print(city);
x= list(city);
print(x);
# ACCESS DICTIONARY
y= city[3];
print(y);
# UPDATE DICTIONARY
poly= {1:"GPP",2:"GPA",3:"GPN"};
engi= {4:"COEP",5:"PICT",2:"VIT"};
poly.update(engi);
print(poly);
# DELETE DICTIONARY
city.clear();
print(city);

# Write a Python script to sort (ascending and descending) a dictionary by value. 
college= {"GPP":9, "GPA":7, "GPK":3,"GPAN":1};
ascend= sorted(college.items(),key= lambda x:x[1]);
convert1= dict(ascend);
print("Ascending sort:")
print(convert1);
descend= sorted(college.items(),key= lambda x:x[1],reverse= True);
convert2= dict(descend);
print("Descending sort:")
print(convert2);

# Write a Python script to concatenate following dictionaries to create a new one. 
dic1 = {1:10, 2:20};
dic2 = {3:30, 4:40};
dic3 = {5:50,6:60};
print("Concatenate two dictionaries:");
dict= {**dic1,**dic2,**dic3};
print(dict);

# Python program to combine two dictionary adding values for common keys.
d1 = {'a': 100, 'b': 200, 'c':300};
d2 = {'a': 300, 'b': 200, 'd':400};
print(d1);
print(d2);
print("adding values for common keys:")
c= {i:d1.get(i,0)+ d2.get(i,0) for i in set(d1).union(d2)}
print(c);

# Python program to print all unique values in a dictionary. 
num= [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},{"VII":"S005"}, {"V":"S009"}, {"VIII":"S007"}]
unique= set(val for dic in num for val in dic.values())
print(unique);


