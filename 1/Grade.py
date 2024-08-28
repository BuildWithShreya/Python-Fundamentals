a=int(input("Enter marks of a Sub 1 :"))
b=int(input("Enter marks of a Sub 2 :"))
c=int(input("Enter marks of a Sub 3 :"))
d=int(input("Enter marks of a Sub 4 :"))
e=int(input("Enter marks of a Sub 5 :"))
total=a+b+c+d+e
print("Total \t\t:",total)
per=(total*100)/5
print("Percentage\t:",per)
if(per>100 and per<90):
    print("A grade !")
elif(per>89 and per<80):
    print("B grade !")
else:
    print("C grade !")