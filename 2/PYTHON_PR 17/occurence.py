# count

f= open("gpp.txt",'r')
content= f.read()
data= content.count('a')
print("How many times 'a' is occur in a gpp.txt file:",data)