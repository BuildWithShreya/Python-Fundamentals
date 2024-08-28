# file creation

with open("sara.txt",'w') as f:
    f.write("Government Polytechnic Pune")
    f.write("\nYou have to do it")
    f.write("\nYou can do it")
f.close()

f= open("sara.txt",'r')
print("Content of File:",f.read())
f.close()

f= open("sara.txt",'r')
print("Content of File:",f.read(10))
f.close()

with open("sara.txt",'r') as f:
    data= f.readlines()
    for line in data:
        word= line.split()
        print(word)
        
f= open("D:\PYTHON PRACTICE\gpp.txt",'r')
print("Content of File:",f.read(10))
f.close()
        

        

