for i in range(1,11):
    if(i==5):
        continue
    print(i)
    
start= int(input("Enter start number: "))
end= int(input("Enter end number: "))
print("Even Numbers: ")
for i in range(start,end+1):
    if(i%2!=0):
        continue
    print(i)
print("Odd Numbers: ")
for i in range(start,end+1):
    if(i%2==0):
        continue
    print(i)
    
text= "Government Polytechnic Pune"
for char in text:
    if(char=='e'):
        continue
    print(char,end="")
 
print()

name= "Government Polytechnic Pune"
for char in text:
    if(char=='c'):
        break
    print(char,end="")

print()

col= "Government Polytechnic Pune"
for char in col:
    if(char.lower()=='e'):
        pass
    else:
        print(char,end="")

print()
        
first= int(input("Enter start: "))
last= int(input("Enter last: "))
print("Even Numbers: ")
for i in range(first,last+1):
    if(i%2==0):
        print(i)
    else:
        pass
print("Odd Numbers: ")
for i in range(first,last+1):
    if(i%2!=0):
        print(i)
    else:
        pass
     
print()

for i in range(10):
    if(i!= 5):
        print(i)
    else:
        break
    











