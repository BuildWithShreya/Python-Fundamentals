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
print("Concatenate dictionaries:");
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

college= {1:"gpp",2:"gpa",3:"gpan",4:"gpk"}
college[5]= "gpd"
print(college)

del college[3]
print(college)

print(college.keys())
print(college.values())
print(len(college))
print(college[4])

p= {1:'sai',2:'sara',3:'siddhi'}
p.pop(1)
print(p)
p.popitem()
print(p)

q= p.copy()
print(q)

k= {1:'android',2:'python',3:'java',4:'c++'}
print(max(k))
print(min(k))
print(k.get(3))

d= {1:'one',2:'three'}
d1= {2:'two'}
d.update(d1)
print(d)
d2={3:'three'}
d.update(d2)
print(d)

# python program to find highest three values in dictionary

a= {'a':16, 'b':43, 'c':21, 'd':98, 'm':104, 'n':435}
sorted_items= sorted(a.items(),key=lambda x:x[1],reverse=True)
highest_three= sorted_items[:3]
print("Highest values in a dictionary:")
for item in highest_three:
    print(item[0],":",item[1])
    
    
dictionary= {"MSBTE": 'Maharashtra State Board of Technical Education', 'CO': 'Computer Engineering', 'SEM': 'Sixth'}
del dictionary['CO']
for key, values in dictionary.items():
    print(key)
dictionary.clear()
for key, values in dictionary.items():
    print(key)
del dictionary


dictionary1= {'Google':1,'Facebook':2,'Microsoft':3}
dictionary2= {'GFG':1,'Microsoft':2,'YouTube':3}
dictionary1.update(dictionary2)
for key, values in dictionary1.items():
    print(key,values)
    
temp= dict()
temp['key1']= {'key1':44, 'key2': 566}
temp['key2']= [1,2,3,4]
for(key, values) in temp.items():
    print(values, end= "")









