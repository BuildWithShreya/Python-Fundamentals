p= int(input("Enter number:"))
m= p
reverse= 0
while(m>0):
    rem= m%10
    reverse= (reverse*10)+rem
    m= m//10
print("Reverse of",p,"is",reverse)